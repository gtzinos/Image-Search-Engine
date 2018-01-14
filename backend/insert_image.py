from flask import Flask
from flask import request
from libs.image_calculations.features import get_features
from flask import jsonify

app = Flask(__name__)
app.Debug = True

@app.route("/")
def hello():
    features()
    return "<h1>Hello There!</h1>"

@app.route("/upload", methods=['POST'])
def upload():
    return 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')