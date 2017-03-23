from .config import *
import datetime
from .saltcoins import Coins

class Timers(object):
    def __init__(self):
        self.now = datetime.datetime.now()
        self.CoinsCurrentMin = self.now.minute
        self.betsCurrentMin = self.now.minute+1
        self.coins = Coins()

    def betTimer(self,mins=2):
        now = datetime.datetime.now()
        newMin = now.minute
        if self.betsCurrentMin < newMin:
            self.betsCurrentMin = newMin+1
            return False
        else:
            return True

    def minuteCoinsTimer(self):
        now = datetime.datetime.now()
        newMin = now.minute
        if self.CoinsCurrentMin < newMin:
            self.CoinsCurrentMin = newMin
            self.coins.timedCoins()