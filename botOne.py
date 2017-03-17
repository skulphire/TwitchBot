from Scripts.Bot_1 import bot
from Scripts.Bot_1.config import *
from Scripts.Bot_1 import APIDriver
from Scripts.Bot_1 import saltcoins
from Scripts.Bot_1 import SocketHandler
from Scripts.Bot_1 import Timers
import json
import time




if __name__ == '__main__':
    f = "usercoins.json"
    coinlib = {}
    try:
        with open(f,'r') as file:
            coinlib = json.load(file)
    except:
        print("usercoins.json not found. File will be created")

    USERCOINS.update(coinlib)

    socket = SocketHandler.SockHandle()
    s = socket.s

    timer = Timers.Timers()

    coins = saltcoins.Coins()

    command = bot.Bot()

    APIDriver = APIDriver.APIDriver()
    followers = input("How many followers? ")
    APIDriver.getAllFollowers(followers)

    command.chat(s, "Connected!")

    try:
        while True:
                user, msg = socket.responses()
                if not user == "*":
                    print(user + ": " + msg)
                timer.minuteCoinsTimer()
                APIDriver.updateViewers(MOD)
                APIDriver.updateViewers(VIEWERS)
                if APIDriver.getNewFollowers():
                    ar = []
                    for index in range(0,len(NEWFOLLOWERS)):
                        newName = "@"+NEWFOLLOWERS[index]
                        ar.append(newName)
                    command.chat(s,"Welcome! "+str(ar))
                    APIDriver.addNewToAll()

                if not msg == "*":
                    if ("!getcoins" or "!GetCoins" or "!Getcoins" or "!getCoins") in msg:
                        #print(msg)
                        command.getDefaultCoins(s,user)
                        command.chat(s,user+" has recieved "+DEFAULTCOIN+" coins")
                    elif ("!coins") in msg:
                        try:
                            command.chat(s,user + " has " +str(coins.checkCoins(user)) + " coins")
                            #print(str(coins.checkCoins(user)))
                        except Exception:
                            print("No value yet")
                    elif ("!bet") in msg:
                       list = msg.split(" ")
                       amount = list[1]
                       option = list[2]

    except KeyboardInterrupt:
        print("Coins:\n"+str(USERCOINS))
        command.chat(s,"Goodbye!")
        with open(f,'w') as file:
            json.dump(USERCOINS,file)