from .config import *

class Better(object):
    def percentages(self):
        win = len(BETWIN)
        lose = len(BETLOSE)

        winPercent = win/(win+lose)*100
        losePercent = abs(winPercent-100)

        return winPercent, losePercent

    def payouts(self, outcome):

        #WIN
        if outcome == 1:
            winners = len(BETWIN)
            totalCoins = self.addAllCoins()
            extra = (totalCoins/winners)
            for user in BETWIN:
                coinsWon = BETWIN[user]*3.42
                coinsWon += extra
                USERCOINS[user] = USERCOINS[user]+coinsWon
        #LOSE
        elif outcome == 2:
            winners = len(BETLOSE)
            totalCoins = self.addAllCoins()
            extra = (totalCoins / winners)
            for user in BETLOSE:
                coinsWon = BETLOSE[user] * 3.42
                coinsWon += extra
                USERCOINS[user] = USERCOINS[user] + coinsWon

    def addAllCoins(self):
        win = sum(BETWIN.values())
        lose = sum(BETLOSE.values())
        total = win+lose
        return total