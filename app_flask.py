import os
from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
   return url_for('.', filename='index.html')

app.run(port=int(os.environ.get('PORT')),host='0.0.0.0')
