import os

from msvcrt import getch

class Winloss(object):
    def __init__(self):
        self.key = ord(getch())
        self.win = 0
        self.winPercent = 0
        self.lose = 0
        self.losePercent = 0
        #self.usefile()



    def usefile(self):
        f = "winloss.txt"
        try:
            file = open(f,'r')
        except:
            print("File not found, creating...")
            file = open(f,'w')
            self.writeFileInitial(file)

    def writeFileInitial(self, file):
        file.write("Win: %d(%d%%)      Loss: %d(%d%%)" % (self.win, self.winPercent, self.lose,self.losePercent))
        file.close()

    def counting(self):
        while True:
            #self.key = ord(getch())
            print(ord(getch()))
