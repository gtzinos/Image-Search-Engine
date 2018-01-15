from flask import Flask, Response, request, json
from flask import request
from libs.image_calculations.features import get_features
from flask import jsonify
from libs.constants.http_codes import HttpCodes

app = Flask(__name__)
app.Debug = True

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route("/upload", methods=['POST'])
def upload():
    return Response(json.dumps({"message": "done"}),
                    status=HttpCodes.HTTP_OK_BASIC,
                    mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0')