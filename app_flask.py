import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return '<h1>Hello World</h1>'
app.run(port=int(os.environ.get('PORT')),host='0.0.0.0')
