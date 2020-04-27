#!usr/bin/env python
import requests

fname = ""
def download(url):
    global fname 
    fname = url.split("/")[-1]
    get_request = requests.get(url)
    print(get_request)
    with open(fname, "wb") as output_file:
        output_file.write(get_request.content)
    

download("https://upload.wikimedia.org/wikipedia/en/1/11/Punk%27d_logo.jpg")
