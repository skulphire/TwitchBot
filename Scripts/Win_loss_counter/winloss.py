import os

class Winloss(object):
    def __init__(self):
        self.outcome = 0
        self.shots = 0
        self.win = 0
        self.winPercent = 0
        self.lose = 0
        self.losePercent = 0
        self.wltext = "winloss.txt"
        self.shottext = "shots.txt"
        self.vars = "vars.txt"
        self.usefile()


    def usefile(self):
        try:
            file = open(self.wltext, 'r')
        except:
            print("File not found, creating...")
            file = open(self.wltext, 'w')
            self.writeFile(file)
        try:
            file = open(self.shottext, "r")
        except:
            print("File not found, creating...")
            file = open(self.shottext, 'w')
            self.writeShots(file)
        try:
            file = open(self.vars, "r")
        except:
            print("File not found, creating...")
            file = open(self.vars, 'w')
            self.writeVars(file)

    def writeVars(self, file):
        file.write("%s" % (self.outcome))
        file.close()

    def writeShots(self,file):
        file.write("%s" % (self.shots))
        file.close()

    def writeFile(self, file):
        file.write("Win: %d(%d%%)      Loss: %d(%d%%)" % (self.win, self.winPercent, self.lose,self.losePercent))
        file.close()

    def percentages(self):
        self.winPercent = self.win / (self.win + self.lose) * 100  # percent increase - abs(((self.win - oldWin)/oldWin)*100)
        self.losePercent = abs(self.winPercent - 100)
        file = open(self.wltext, 'w')
        self.writeFile(file)

    def countWinLoss(self):
        while True:
            update = input(": ")
            if update == "win":
                self.win = self.win+1
                self.percentages()
            elif update == "lose":
                self.lose = self.lose+1
                self.percentages()
            elif update == "shot":
                self.shots += 1
                file = open(self.shottext,"w")
                self.writeShots(file)
            elif update == "setshot0":
                self.shots = 0
                file = open(self.shottext, "w")
                self.writeShots(file)
            elif update == "setwl0":
                self.lose = 0
                self.win = 0
                self.winPercent = 0
                self.losePercent = 0
                file = open(self.wltext, 'w')
                self.writeFile(file)