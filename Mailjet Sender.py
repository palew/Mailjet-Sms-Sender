from email import header
import requests
import json
import ctypes
from os import system

print("""

            @riksouleclown

            https://github.com/cozyz


""")

system("title " + "cozyz")
file = open("num.txt", "r")
lines = file.readlines()
for line in lines:
    r = requests.post('https://api.mailjet.com/v4/sms-send',{"Text": "Have a nice SMS flight with Mailjet !","To": "+33"+line,"From": "MJPilot"},headers={"Authorization": "Bearer XXX","Content-Type":"application/json"})
    print(r.content)
file.close
print("")
print("Task is finish")
print("")
system("pause")