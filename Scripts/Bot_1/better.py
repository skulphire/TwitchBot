from .config import *

class Better(object):
    def percentages(self):
        win = len(BETWIN)
        lose = len(BETLOSE)

        winPercent = win/(win+lose)*100
        losePercent = abs(winPercent-100)

        return winPercent, losePercent

    def payouts(self):
        #WIN
        if OUTCOME == 1:
            winners = len(BETWIN)
            totalCoins = self.addAllCoins()


    def addAllCoins(self):
        win = sum(BETWIN.values())
        lose = sum(BETLOSE.values())
        total = win+lose
        return total