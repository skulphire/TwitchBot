from .config import *
import time

class Coins(object):
    def addUser(self,user):
        USERCOINS[user] = 0

    def checkCoins(self,user):
        return USERCOINS[user]

    def timedCoins(self):
        for viewer in CURRENTVIEWERS:
            USERCOINS[viewer] = USERCOINS[viewer]+MINUTECOIN

    def assignCoins(self, user):
        if user in ALLFOLLOWERS:
            USERCOINS[user] = USERCOINS[user]+FOLLOWREWARD