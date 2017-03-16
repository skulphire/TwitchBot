from Scripts.Win_loss_counter.winloss import Winloss
from Scripts.Bot_1 import bot
from Scripts.Bot_1.config import *
from Scripts.Bot_1 import APIDriver
from Scripts.Bot_1 import saltcoins
from Scripts.Bot_1 import SocketHandler
from Scripts.Bot_1 import Timers
import time

if __name__ == '__main__':
    socket = SocketHandler.SockHandle()
    s = socket.s

    wlCounter = Winloss()

    timer = Timers.Timers()

    coins = saltcoins.Coins()
    command = bot.Bot()
    APIDriver = APIDriver.APIDriver()

    followers = input("How many followers? ")
    APIDriver.getAllFollowers(followers)

    command.chat(s, "Connected!")

    while True:
            user, msg = socket.responses()
            timer.minuteCoinsTimer()
            consoleIn = input(": ")
            if consoleIn == "1" or consoleIn == "2" or consoleIn == "set0":
                wlCounter.countWinLoss(consoleIn)
            #if "!bet" in msg:
            #    list = message.split(" ")
            #    amount = list[1]
            #    option = list[2]
