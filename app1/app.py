# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route("/app1")
def home():
    return """<h1>This is app1!</h1>
              <img src='static/images/flask-badge-1.png'/>"""

if __name__ == '__main__':
    app.run() 
