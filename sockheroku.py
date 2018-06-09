import os
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('',int(os.environ['PORT'])))
server.listen(2)
while True:
    conn,addr=server.accept()
    conn.send("hello from heroku")