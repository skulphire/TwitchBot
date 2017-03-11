import os




class Winloss(object):
    def __init__(self):
        self.win = 0
        self.winPercent = 0
        self.lose = 0
        self.losePercent = 0
        self.f = "winloss.txt"
        self.usefile()



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

    def countWinLoss(self):
        while True:
            oldWin = self.win
            update = input("win(1),loss(2): ")
            if update == "1":
                self.win = self.win+1
            elif update == "2":
                self.lose = self.lose+1
            elif update == "0":
                self.lose = 0
                self.win = 0

            self.winPercent = self.win/(self.win+self.lose)*100 #percent increase - abs(((self.win - oldWin)/oldWin)*100)
            self.losePercent = abs(self.winPercent-100)
            file = open(self.f, 'w')
            self.writeFile(file)
            file.close()