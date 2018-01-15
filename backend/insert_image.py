from flask import Flask, Response, request, json
from flask import request
#from libs.image_calculations.features import get_features
from flask import jsonify
from libs.constants.http_codes import HttpCodes
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

app.Debug = True

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
                status=HttpCodes.HTTP_BAD_REQUEST,
                mimetype='application/json')

    for file in request.files.getlist('file'):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return Response(json.dumps({"message": "done"}),
                    status=HttpCodes.HTTP_OK_BASIC,
                    mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0')