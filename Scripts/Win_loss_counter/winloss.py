import os
import Scripts.Bot_1.config as config
from Scripts.Bot_1 import better

class Winloss(object):
    def __init__(self):
        self.win = 0
        self.winPercent = 0
        self.lose = 0
        self.losePercent = 0
        self.f = "winloss.txt"
        self.usefile()
        self.bets = better.Better()

    def usefile(self):
        try:
            file = open(self.f,'r')
        except:
            print("File not found, creating...")
            file = open(self.f,'w')
            self.writeFile(file)

    def writeFile(self, file):
        file.write("Win: %d(%d%%)      Loss: %d(%d%%)" % (self.win, self.winPercent, self.lose,self.losePercent))
        file.close()

    def percentages(self):
        self.winPercent = self.win / (self.win + self.lose) * 100  # percent increase - abs(((self.win - oldWin)/oldWin)*100)
        self.losePercent = abs(self.winPercent - 100)
        file = open(self.f, 'w')
        self.writeFile(file)

    def countWinLoss(self):
        while True:
            update = input("win(1),loss(2): ")
            if update == "1":
                self.win = self.win+1
                outcome = 1
                self.bets.payouts(outcome)
                self.percentages()
            elif update == "2":
                self.lose = self.lose+1
                outcome = 2
                self.bets.payouts(outcome)
                self.percentages()
            elif update == "set0":
                self.lose = 0
                self.win = 0
                self.winPercent = 0
                self.losePercent = 0
                file = open(self.f, 'w')
                self.writeFile(file)