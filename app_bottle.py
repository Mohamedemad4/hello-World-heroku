import os
import bottle
@bottle.route("/<staticfile>")
@bottle.route("/")
def hello_world(staticfile):
    if staticfile==None:
       staticfile='index.html' 
    return bottle.static_file(root='.',filename=staticfile)
bottle.run(port=int(os.environ.get('PORT')),host='0.0.0.0')
