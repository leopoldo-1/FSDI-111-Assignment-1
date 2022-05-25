from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
  return "<h1><u>Assignment 1</u></h1> <br> <h3>endpoint /aboutme</h3>"

@app.get("/aboutme")
def about_me():
  me = {
    "first_name": "Leopoldo",
    "last_name": "Miranda",
    "hobby": "Play the guitar"
  }
  return me