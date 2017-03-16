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

    timer = Timers.Timers()

    coins = saltcoins.Coins()
    command = bot.Bot()
    APIDriver = APIDriver.APIDriver()

    followers = input("How many followers? ")
    APIDriver.getAllFollowers(followers)

    command.chat(s, "Connected!")

    #thread for reading chat
    # readChat = threading.Thread(target=socket.responseThread())
    # readChat.daemon = True
    # readChat.start()
    # print("Started chat thread...")
    #
    # minute = threading.Thread(target=socket.minuteTimer())
    # minute.daemon = True
    # minute.start()
    # print("Started minute thread...")

    while True:
            user, msg = socket.responses()
            timer.minuteTimer()

            #if "!bet" in msg:
            #    list = message.split(" ")
            #    amount = list[1]
            #    option = list[2]

