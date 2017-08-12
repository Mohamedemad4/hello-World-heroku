import os
import bottle

@bottle.route("/<staticfile>")
def hello_world(staticfile):
    return bottle.static_file(root='.',filename=staticfile)

@bottle.route('/')
def re():
    bottle.redirect('/index.html')
    
bottle.run(port=int(os.environ.get('PORT')),host='0.0.0.0')
