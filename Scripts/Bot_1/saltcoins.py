from .config import *

class Coins(object):
    def checkCoins(self,user):
        return USERCOINS[user]

    def assignCoins(self, user):
        if user in ALLFOLLOWERS:
            USERCOINS[user] = USERCOINS[user]+FOLLOWREWARD
        else:
            USERCOINS[user] = 0