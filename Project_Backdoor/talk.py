#!/usr/bin/env python3
'''
Do this on hacker machine:

nc -vv -l -p 4444
netcat verbose listen port 4444


Run this code on the target:

'''
import socket
def connect_to(ip, port):
    # create a socket object
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect 
    connection.connect((ip, port))
    connection.send("\n[INFO] Connection Established".encode("utf-8"))
    print("[INFO] Connection Established")
    return connection

def send_str(connection, stringMessage):
    connection.send(("\n" + stringMessage + "\n").encode("utf-8"))
    return

pipe = connect_to("192.168.1.197", 4444)
while (True):
    stringMessage = input("[MESSAGE] : ")
    send_str(pipe, stringMessage)
    if(stringMessage.strip() == "close"):
        break

pipe.close()



