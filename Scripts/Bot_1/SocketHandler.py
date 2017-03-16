from .config import *
from .bot import CHAT_MSG
import socket
import re
import time
import select

class SockHandle(object):
    def __init__(self):
        self.s = socket.socket()

        try:
            self.s.connect((HOST, PORT))
        except Exception:
            self.s.connect((HOST, WEB_PORT))

        self.s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
        self.s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
        self.s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))
        self.s.setblocking(0)

    def responses(self):
        #checks for data
        ready = select.select([self.s],[],[],1)
        if ready[0]:
            response = self.s.recv(1024).decode("utf-8")
            if response == "PING :tmi.twitch.tv\r\n":
                self.s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            else:
                username = re.search(r"\w+", response).group(0)  # return the entire match
                message = CHAT_MSG.sub("", response)
                #print(username + ": " + message)
                return username, message