from .config import *
#from .saltcoins import Coins
import re
import json

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
class Bot(object):
    #def __init__(self):
        #self.coins = Coins()

    def chat(self,sock,msg):
        """
           Send a chat message to the server.
           Keyword arguments:
           sock -- the socket over which to send the message
           msg  -- the message to be sent
           """
        sender = "PRIVMSG " + CHAN + " :" + msg +"\r\n"
        sock.send(sender.encode())

    def ban(self,sock,user):
        """
            Ban a user from the current channel.
            Keyword arguments:
            sock -- the socket over which to send the ban command
            user -- the user to be banned
            """
        self.chat(sock,".ban {}".format(user))

    def timeout(self,sock,user,secs=600):
        """
           Time out a user for a set period of time.
           Keyword arguments:
           sock -- the socket over which to send the timeout command
           user -- the user to be timed out
           secs -- the length of the timeout in seconds (default 600)
           """
        self.chat(sock, ".timeout {}".format(user,secs))

    def bets(self,sock,user,amount,option):
        if amount > USERCOINS[user]:
            self.chat(sock,user+" - You don't have enough SaltCoins!")
        else:
            if option == "1":
                BETDICTFOR[user] = amount
            elif option == "2":
                BETDICTAGAINST[user] = amount
            USERCOINS[user] = USERCOINS[user]-amount