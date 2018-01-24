import os
import sys

from flask import Flask, Response, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from werkzeug.utils import secure_filename
from config.app_config import AppConfig

from utils.constants.http_codes import HttpCodes
from utils.image_calculations.features import get_features, cut_dimensions
from utils.image_calculations.size import convert_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = str(AppConfig.public_upload_folder)
app.config['MAX_CONTENT_LENGTH'] = AppConfig.max_image_length
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + str(AppConfig.database_user) + ':' + str(AppConfig.database_password) + '@' + str(AppConfig.database_host) + ':' + str(AppConfig.database_port) + "/" + str(AppConfig.database_name)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.Debug = True 

# initialize the database connection
db = SQLAlchemy(app)

# initialize database migration management
#MIGRATE = Migrate(APP, DB)

from Picture import *

#Init datab
db.create_all()
db.session.commit()

#Allowed image types
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Enable cross-origin requests
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

#Search image similarity rest api
@app.route("/search", methods=['POST'])
def search():

    if len(request.files) == 0:
        return Response(json.dumps({"message": "No file part"}),
                status = HttpCodes.HTTP_BAD_REQUEST,
                mimetype='application/json')
    #Distance metric
    selectedMetric = request.form.get('selectedMetric')
    #KNN Number
    selectedNumber = request.form.get('selectedNumber')
    #Search in all features array
    searchAllFeatures = request.form.get('searchAllFeatures')
    #Init images array (Response)
    images = []

    for file in request.files.getlist('file'):
        
        if file and allowed_file(file.filename):

            #Filter image name
            filename = secure_filename(file.filename)

            #Build path
            path = os.path.join("./", filename)

            try:
                #Resize image
                image = convert_image(file, 200, 200)
                
                #Store image
                image.save(path)

                #Get descriptor vector
                (kp, features) = get_features(path)

                #Delete file
                if os.path.exists(path):
                    os.remove(path)
                
                #Define distance metric operator
                metric = "<->"
                if selectedMetric == 1:
                    metric = "<#>"
                elif selectedMetric == 2:
                    metric = "<=>"

                featuresToSearch = features.tolist()
                featuresFieldName = "features"
                if searchAllFeatures == "false":
                    featuresToSearch = cut_dimensions(features).tolist()
                    featuresFieldName = "cut_features"

                #Get common images
                command = text("select cube(" + str(featuresFieldName) + ") " + str(metric) + " cube(:vector2) as distance, filename from pictures order by distance limit " + str(selectedNumber))
                
                #Execute command            
                data = db.engine.execute(command, vector2=featuresToSearch).fetchall()

                #Calculate response
                for (distance, filename) in data:
                    images.append({"distance": distance, "url": os.path.join(AppConfig.public_image_url, filename)})

            except:
                #Delete file
                if os.path.exists(path):
                    os.remove(path)

                e = sys.exc_info()[0]
                return Response(json.dumps({"message": str(e)}),
                    status = HttpCodes.HTTP_BAD_FORBIDDEN,
                    mimetype = 'application/json') 

            return Response(json.dumps({"message": images}),
                status = HttpCodes.HTTP_OK_BASIC,
                mimetype = 'application/json')

        else:
            return Response(json.dumps({"message": "No file part"}),
                status = HttpCodes.HTTP_BAD_REQUEST,
                mimetype='application/json')
            

    return Response(json.dumps({"message": "done"}),
        status = HttpCodes.HTTP_OK_BASIC,
        mimetype = 'application/json')


#Insert new image in database rest api
@app.route("/upload", methods=['POST'])
def upload():
     # check if the post request has the file part
    if len(request.files) == 0:
        return Response(json.dumps({"message": "No file part"}),
                status = HttpCodes.HTTP_BAD_REQUEST,
                mimetype='application/json')
    
    
    for file in request.files.getlist('file'):
        if file and allowed_file(file.filename):
            
            #Filter image name
            filename = secure_filename(file.filename)

            #Build path
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            try:
                #Resize image
                image = convert_image(file, 200, 200)
                
                #Store image
                image.save(path)

                #Get descriptor vector
                (kp, features) = get_features(path)
                
                #Cut dimensions of kp
                kp_cut = cut_dimensions(kp)

                #Cut dimensions of features
                features_cut = cut_dimensions(features)

                #Create image instance
                image = Picture(kp.tolist(), features.tolist(), kp_cut.tolist(), features_cut.tolist(), filename)   

                try:
                    #Insert image in database
                    db.session.add(image)
                    db.session.commit()
                except:
                    db.session.rollback()

                    #Delete file
                    if os.path.exists(path):
                        os.remove(path)

                    e = sys.exc_info()[0]
                    return Response(json.dumps({"message": str(e)}),
                        status = HttpCodes.HTTP_BAD_FORBIDDEN,
                        mimetype = 'application/json')

            except:
                #Delete file
                if os.path.exists(path):
                    os.remove(path)

                e = sys.exc_info()[0]
                return Response(json.dumps({"message": str(e)}),
                    status = HttpCodes.HTTP_BAD_FORBIDDEN,
                    mimetype = 'application/json') 

                    
    return Response(json.dumps({"message": "done"}),
        status = HttpCodes.HTTP_OK_BASIC,
        mimetype = 'application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
