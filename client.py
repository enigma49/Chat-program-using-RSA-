import socket
import sys
import time

s = socket.socket()
host = input(str("Enter the server's name: "))
port = 8080
s.connect((host,port))
print("Connected to the server")
while 1 :
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server:",incoming_message)
    message = input(str(""))
    message = message.encode()
    s.send(message)
