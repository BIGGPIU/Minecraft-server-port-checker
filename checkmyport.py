import os
from time import sleep
from requests import get
import socket
global x
global y
global ip
x = 0
y = 0
ip = get("https://api.ipify.org").content.decode("utf8")
f = open("settings.txt","r")
hold = f.read()
port = hold.replace("PORT=","")
port = int(port)
print (f"Checking port {port} on IP {ip}")
def checkIPchange():
    global ip
    if ip != get("https://api.ipify.org").content.decode("utf8"):
        ip = get("https://api.ipify.org").content.decode("utf8")
def checkifonline():
    global x 
    global y
    global port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((f"{ip}",port))
    if result == 0:
        if x == 0:
            print ("The server is online")
            x = x+1
            y = 0
        if x != 0:
            return
    else: 
        if y == 0:
            print ("The server is offline")
            y = y+1
            x = 0
        if y != 0:
            return


while __name__ == "__main__":
    checkifonline()
    sleep(10)
    checkIPchange()
#print ("my ip is: {}".format(ip))
#so now the program can tell if the server is online or not. now to just make it check again and again and print if its online.
#oops
#now that it constantly checks if its online or not I now have to make it so now it wont repeat the same statement.