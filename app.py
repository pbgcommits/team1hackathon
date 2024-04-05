from flask import Flask, jsonify, request
from bson import ObjectId

app = Flask(__name__)

@app.route("/")
def Team1():
    return "Hello, Team1!"
