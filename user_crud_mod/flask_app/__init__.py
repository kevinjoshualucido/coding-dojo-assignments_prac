from flask import Flask, session
app = Flask(__name__)
app.secret_key = "This a secret key lol."