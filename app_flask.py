import os
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/<staticfile>')
def hello_world(staticfile):
   return open(staticfile,'rb').read()

@app.route('/')
def re():
    return redirect('/index.html')
  
app.run(port=int(os.environ.get('PORT')),host='0.0.0.0')
