from flask import Flask
import os
var = os.getenv("VARIABLE_MSG")
password = os.getenv("PASSWORD")
app = Flask(__name__)

@app.route("/app")
def hello():
    returnString = var + " " + password
    return returnString
