import socket
import sys

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

clientsocket.connect((host, port))
clientsocket.close()
