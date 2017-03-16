from Scripts.Bot_1 import bot
from Scripts.Bot_1.config import *
from Scripts.Bot_1 import APIDriver
from Scripts.Bot_1 import saltcoins
from Scripts.Bot_1 import SocketHandler
from Scripts.Bot_1 import Timers
import json
import os
import time




if __name__ == '__main__':
    f = "usercoins.json"
    try:
        with open(f,'r') as file:
            USERCOINS = json.load(file)
    except:
        print("usercoins.json not found. File will be created")

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
    try:
        while True:
                user, msg = socket.responses()
                if not user == "*":
                    print(user + ": " + msg)
                timer.minuteCoinsTimer()

                if "!getcoins" or "!GetCoins" or "!Getcoins" or "!getCoins":
                    command.getDefaultCoins(s,user)

                #if "!bet" in msg:
                #    list = message.split(" ")
                #    amount = list[1]
                #    option = list[2]
    except KeyboardInterrupt:
        input()
        with open(f,'w') as file:
            json.dump(USERCOINS,file)