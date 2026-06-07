import socket

server = socket.create_server(('', 9999))
connection, address = server.accept()

connection.send(b'This is IoT world!!!')
connection.close()

