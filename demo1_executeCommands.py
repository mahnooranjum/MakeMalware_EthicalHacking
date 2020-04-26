#!usr/bin/env python
import subprocess

command = "msg * you've been fooled"
subprocess.Popen(command, shell=True)
