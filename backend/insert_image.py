from flask import Flask
app = Flask(__name__)
app.Debug = True

@app.route("/")
def hello():
    return "<h1>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')