from flask import Flask, Response, request, json
from flask import request
from libs.image_calculations.features import get_features
from flask import jsonify
from libs.constants.http_codes import HttpCodes
from werkzeug.utils import secure_filename
import os
from libs.image_calculations.size import convert_image
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1994gt31@localhost:5432/image_search_engine'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'svg'])
app.Debug = True

#db = sqlalchemy.create_engine('postgresql://postgres:1994gt31@localhost:5432/image_search_engine')  
#engine = db.connect()  

# initialize the database connection
db = SQLAlchemy(app)

# initialize database migration management
#MIGRATE = Migrate(APP, DB)

from Picture import *

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route("/upload", methods=['POST'])
def upload():
     # check if the post request has the file part
    print(request.files)
    if len(request.files) == 0:
        return Response(json.dumps({"message": "No file part"}),
                status = HttpCodes.HTTP_BAD_REQUEST,
                mimetype='application/json')
    db.create_all()
    db.session.commit()

    for file in request.files.getlist('file'):
        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            image = convert_image(file, 30, 30)

            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            path = "./uploads/2.jpg"
            vector = get_features(path).tolist()

            image = Picture(vector, path)


            db.session.add(image)
            db.session.commit()

    # Check that email does not already exist (not a great query, but works)
    # if not db.session.query(User).filter(User.email == email).count():
    #    reg = User(email)
    #   db.session.add(reg)
    #   db.session.commit()

    return Response(json.dumps({"message": "done"}),
        status = HttpCodes.HTTP_OK_BASIC,
        mimetype = 'application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0')