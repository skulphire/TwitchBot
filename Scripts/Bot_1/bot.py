from .config import *
import re


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

    def getDefaultCoins(self,sock,user):
        USERCOINS[user] = DEFAULTCOIN

    def bets(self,sock,user,amount,option):
        if int(amount) > USERCOINS[user]:
            self.chat(sock,"@"+user+" - You don't have enough SaltCoins!")
        else:
            if "1" in option:
                BETWIN[user] = int(amount)
                USERCOINS[user] = USERCOINS[user] - int(amount)
            elif "2" in option:
                BETLOSE[user] = int(amount)
                USERCOINS[user] = USERCOINS[user]- int(amount)