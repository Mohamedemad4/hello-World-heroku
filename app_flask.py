import os
from flask import Flask,url_for

app = Flask(__name__)

@app.route('/<staticfile>',default={'staticfile':'index.html'})
def hello_world(staticfile):
   return url_for('.', filename=staticfile)

app.run(port=int(os.environ.get('PORT')),host='0.0.0.0')
