from Scripts.Bot_1 import bot
from Scripts.Bot_1.config import *
from Scripts.Bot_1 import APIDriver
from Scripts.Bot_1 import saltcoins
from Scripts.Bot_1 import SocketHandler
from Scripts.Bot_1 import Timers
from Scripts.Bot_1 import better
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

    bets = better.Better()
    currentBetting = False
    paid = True

    APIDriver = APIDriver.APIDriver()
    followers = input("How many followers? ")
    APIDriver.getAllFollowers(followers)

    command.chat(s, "Connected!")
    try:
        while True:
                user, msg = socket.responses()
                if not user == "*":
                    print(user + ": " + msg)

                if not msg == "*":
                    # if ("!getcoins" or "!GetCoins" or "!Getcoins" or "!getCoins") in msg:
                    #     #print(msg)
                    #     command.getDefaultCoins(s,user)
                    #     command.chat(s,"@"+user+" has recieved "+str(DEFAULTCOIN)+" coins")
                    if ("!coins") in msg:
                        try:
                            command.chat(s,user + " has " +str(coins.checkCoins(user)) + " coins")
                            #print(str(coins.checkCoins(user)))
                        except Exception:
                            print("No value yet")
                    elif ("!bet") in msg:
                       if currentBetting:
                           list = msg.split(" ")
                           amount = list[1]
                           option = list[2]
                           command.bets(s,user,amount,option)
                       else:
                           command.chat(s,"Betting is closed or has not opened!")
                    elif ("!give") in msg:
                        if (APIDriver.checkMod(user) or user == "aphiremarbl"):
                            list = msg.split(" ")
                            userToGift = list[1]
                            amount = list[2]
                            coins.giveCoins(userToGift,amount)
                        else:
                            command.chat(s,"You do not have permission!")
                    elif ("!newbet") in msg:
                        if (APIDriver.checkMod(user) or user == "aphiremarbl"):
                            command.startBet(s)
                            currentBetting = True
                            paid = False
                        else:
                            command.chat(s, "You do not have permission!")


                if currentBetting:
                    if not timer.betTimer():
                        currentBetting = False
                        command.chat(s,"Betting has closed")

                if not paid and not currentBetting:
                    file = open("vars.txt",'r')
                    outcome = file.read()
                    if outcome == "1":
                        bets.payoutsWin()
                    elif outcome == "2":
                        bets.payoutsLose()
                    paid = True
                    file.close()
                    file = open("vars.txt", 'w')
                    file.write("0")
                    file.close()

                timer.minuteCoinsTimer()
                APIDriver.updateViewers(MOD)
                APIDriver.updateViewers(VIEWERS)
                if APIDriver.getNewFollowers():
                    ar = []
                    for index in range(0,len(NEWFOLLOWERS)):
                        newName = "@"+NEWFOLLOWERS[index]
                        ar.append(newName)
                    command.chat(s,"Welcome! Thanks for following! "+str(ar))
                    APIDriver.addNewToAll()

    except KeyboardInterrupt:
        #print("Coins:\n"+str(USERCOINS))
        command.chat(s,"Goodbye!")
        with open(f,'w') as file:
            json.dump(USERCOINS,file)