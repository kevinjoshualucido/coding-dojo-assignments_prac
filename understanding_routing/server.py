from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/dojo")
def dojo():
    return "Dojo!"


@app.route("/say/<croissant>")
def say(croissant):
    return f"Hi {croissant}!"


@app.route("/repeat/<int:num>/<word>")
def repeat(num, word):
    return word * num


if __name__ == "__main__":
    app.run(debug=True, port=5002)
