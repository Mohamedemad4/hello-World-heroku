import bottle
@bottle.route("/")
def hello_world():
    return '<h1>Hello World</h1>'
bottle.run(port=8080,host='0.0.0.0')
