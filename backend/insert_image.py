from flask import Flask, json
from flask import request
from libs.image_calculations.features import get_features
from flask import jsonify

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
    return json.dumps([{"a": 1}])


if __name__ == "__main__":
    app.run(host='0.0.0.0')