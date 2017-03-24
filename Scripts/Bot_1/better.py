from .config import *


class Better(object):
    def percentages(self):
        win = len(BETOPONE)
        lose = len(BETOPTWO)

        winPercent = win/(win+lose)*100
        losePercent = abs(winPercent-100)
        try:
            file = open("odds.txt", 'r')
        except:
            print("File not found, creating...")
            file = open("odds.txt", 'w')
            self.writeFile(file,winPercent,losePercent)

    def writeFile(self, file, win, lose):
        file.write("Odds: (%d%%)W - (%d%%)L" % (win,lose))
        file.close()

    def payoutsOne(self):
        if TYPE == 1:
            pay = 2
        elif TYPE == 2:
            pay = 2
        else:
            pay = 1.5

        winners = len(BETOPONE) + 1
        totalCoins = self.addAllCoins()
        extra = (totalCoins/winners)
        for user in BETOPONE:
            coinsWon = BETOPONE[user] * pay
            coinsWon += extra
            USERCOINS[user] = USERCOINS[user]+int(coinsWon)
        self.clearBets()

    def payoutsTwo(self):
        if TYPE == 1:
            pay = 2
        elif TYPE == 2:
            pay = 1.6
        else:
            pay = 1.5

        winners = len(BETOPTWO) + 1
        totalCoins = self.addAllCoins()
        extra = (totalCoins / winners)
        for user in BETOPTWO:
            coinsWon = BETOPTWO[user] * pay
            coinsWon += extra
            USERCOINS[user] = USERCOINS[user] + int(coinsWon)
        self.clearBets()

    def payoutsThree(self):
        if TYPE == 1:
            pay = 2
        elif TYPE == 2:
            pay = 1.3
        else:
            pay = 1.5
        winners = len(BETOPTHREE) + 1
        totalCoins = self.addAllCoins()
        extra = (totalCoins/winners)
        for user in BETOPTHREE:
            coinsWon = BETOPTHREE[user] * pay
            coinsWon += extra
            USERCOINS[user] = USERCOINS[user]+int(coinsWon)
        self.clearBets()

    def payoutsFour(self):
        if TYPE == 1:
            pay = 2
        elif TYPE == 2:
            pay = 1.1
        else:
            pay = 1.5

        winners = len(BETOPFOUR) + 1
        totalCoins = self.addAllCoins()
        extra = (totalCoins / winners)
        for user in BETOPFOUR:
            coinsWon = BETOPFOUR[user] * pay
            coinsWon += extra
            USERCOINS[user] = USERCOINS[user] + int(coinsWon)
        self.clearBets()

    def payoutsFive(self):
        if TYPE == 1:
            pay = 1.5
        elif TYPE == 2:
            pay = 1.5
        else:
            pay = 1.5
        winners = len(BETOPFIVE) + 1
        totalCoins = self.addAllCoins()
        extra = (totalCoins / winners)
        for user in BETOPFIVE:
            coinsWon = BETOPFIVE[user] * pay
            coinsWon += extra
            USERCOINS[user] = USERCOINS[user] + int(coinsWon)
        self.clearBets()

    def clearBets(self):
        BETOPONE.clear()
        BETOPTWO.clear()
        BETOPTHREE.clear()
        BETOPFOUR.clear()
        BETOPFIVE.clear()

    def addAllCoins(self):
        win = sum(BETOPONE.values())
        lose = sum(BETOPTWO.values())
        three = sum(BETOPTHREE.values())
        four = sum(BETOPFOUR.values())
        five = sum(BETOPFIVE.values())
        total = win+lose+three+four+five
        return total