from Scripts.Bot_1 import bot
from Scripts.Bot_1.config import *
import socket
import time
import re

if __name__ == '__main__':
    s = socket.socket()
    try:
        s.connect((HOST,PORT))
    except Exception:
        s.connect((HOST,WEB_PORT))

    s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

    command = bot.Bot()

    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0) # return the entire match
            message = bot.CHAT_MSG.sub("", response)
            #print(username + ": " + message)
            if "!bet" in message:
                amount = int(message.split(" "))
                print(amount)

        time.sleep(1/RATE)

