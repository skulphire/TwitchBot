from .config import *
import datetime
from .saltcoins import Coins

class Timers(object):
    def __init__(self):
        self.now = datetime.datetime.now()
        self.currentMin = self.now.minute
        self.coins = Coins()

    def minuteCoinsTimer(self):
        now = datetime.datetime.now()
        newMin = now.minute
        if self.currentMin < newMin:
            self.currentMin = newMin
            self.coins.timedCoins()
            print("minute")