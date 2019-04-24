import os
from flask import Flask,redirect,request

app = Flask(__name__)

#@app.route('/<staticfile>')
#def hello_world(staticfile):
#   return open(staticfile,'rb').read()

@app.route('/')
def re():
    return "404 Not found: {0}".format(request.remote_addr)  #redirect('/index.html')
  
app.run(port=int(os.environ.get('PORT')),host='0.0.0.0')
