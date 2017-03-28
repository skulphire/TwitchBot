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

    def whisper(self,sock,user,msg):
        sender = "PRIVMSG " + CHAN + " :" + "/w "+user+" "+msg + "\r\n"
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

    def startBet(self,sock,type):

        if int(type) == 1:
            options = "Options: Win = 1, Lose = 2"
        elif int(type) == 2:
            options = "Options: 1st = 1, 2nd = 2, 3rd = 3, Lose = 4"
        elif int(type) == 3:
            file = open("betType.txt",'r')
            options = file.read()
            file.close()

        announcement = "Betting is open! use !bet amount option to place your bets. Example: !bet 100 1 for betting 100 on option 1"
        self.chat(sock,announcement)
        self.chat(sock, options)

    def getDefaultCoins(self,sock,user):
        USERCOINS[user] = DEFAULTCOIN

    def stateWinners(self,sock,winDict):
        ar = []
        for winner in winDict:
            ar.append("@"+winner)
        self.chat(sock,"Winners are:"+str(ar))

    def bets(self,sock,user,amount,option):
        if int(amount) > USERCOINS[user]:
            self.chat(sock,"@"+user+" - You don't have enough SaltCoins!")
        else:
            if "1" in option:
                BETOPONE[user] = int(amount)
                USERCOINS[user] = USERCOINS[user] - int(amount)
            elif "2" in option:
                BETOPTWO[user] = int(amount)
                USERCOINS[user] = USERCOINS[user]- int(amount)
            elif "3" in option:
                BETOPTHREE[user] = int(amount)
                USERCOINS[user] = USERCOINS[user] - int(amount)
            elif "4" in option:
                BETOPFOUR[user] = int(amount)
                USERCOINS[user] = USERCOINS[user] - int(amount)
            elif "5" in option:
                BETOPFIVE[user] = int(amount)
                USERCOINS[user] = USERCOINS[user] - int(amount)