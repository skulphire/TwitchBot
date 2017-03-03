import os

class Winloss(object):
    def __init__(self):
        self.usefile()

    def usefile(self):
        f = "winloss.txt"
        try:
            file = open(f,'r')
        except:
            print("File not found, creating...")
            file = open(f,'w')