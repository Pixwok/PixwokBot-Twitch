from socket import *
from time import *
from config import *
from getmodo import *


#Global VAR
project = ""
msginfo = ""
date = ""



s = socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHANNEL).encode("utf-8"))

def cmd():
    commandlist = "Voici la liste des commandes: !cmd --> Liste des commandes / !projet --> Affiche le projet en cours / !info --> Programme du live / !next --> Prochain live / !cyberpix --> rejoindre le serveur Minecraft"
    if "PRIVMSG #cappixwok :!cmd\r\n" in response:
        s.send("PRIVMSG {} :{}\r\n".format(CHANNEL, commandlist).encode("utf-8"))

def projet():
    global project
    if "PRIVMSG #cappixwok :!setprojet" in response:
        getmodo()
        for i in modo_list:
            if i in response:
                pos = response.find("!setprojet") + 11
                project = response[pos:]
    if "PRIVMSG #cappixwok :!projet\r\n" in response:
        s.send("PRIVMSG {} :Projet en cours: {}\r\n".format(CHANNEL, project).encode("utf-8"))

def info():
    global msginfo
    if "PRIVMSG #cappixwok :!setinfo" in response:
        getmodo()
        for i in modo_list:
            if i in response:
                pos = response.find("!setinfo") + 9
                msginfo = response[pos:]
    if "PRIVMSG #cappixwok :!info\r\n" in response:
        s.send("PRIVMSG {} :{}\r\n".format(CHANNEL, msginfo).encode("utf-8"))

def next():
    global date
    if "PRIVMSG #cappixwok :!setnext" in response:
        getmodo()
        for i in modo_list:
            if i in response:
                pos = response.find("!setnext") + 9
                date = response[pos:]
    if "PRIVMSG #cappixwok :!next\r\n" in response:
        s.send("PRIVMSG {} :Prochain live le {}\r\n".format(CHANNEL, date).encode("utf-8"))

def cyberpix():
    msg = "Rejoindre le serveur CyberPix https://docs.google.com/forms/d/e/1FAIpQLScbMKxQqN6VdiZH3Dxy46VawFz__uZWau6C6fF6mW_KBaWx5Q/viewform?usp=pp_url"
    if "PRIVMSG #cappixwok :!cyberpix\r\n" in response:
        s.send("PRIVMSG {} :{}\r\n".format(CHANNEL, msg).encode("utf-8"))
while True:
    response = s.recv(1024).decode("utf-8")
    print(response)
    cmd()
    projet()
    info()
    next()
    cyberpix()
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    sleep(0.1)