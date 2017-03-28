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
    type = ""

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
                    if ("!coin" or "!coins") in msg:
                        try:
                            command.whisper(s,user,"You have "+str(coins.checkCoins(user)) + " coins")
                            #command.chat(s,user + " has " +str(coins.checkCoins(user)) + " coins")
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
                    elif ("!add") in msg:
                        if (APIDriver.checkMod(user) or user == "aphiremarbl"):
                            list = msg.split(" ")
                            userToGift = list[1]
                            amount = list[2]
                            coins.giveCoins(userToGift,amount)
                        else:
                            command.chat(s,"You do not have permission!")
                    elif ("!newbet") in msg:
                        if (APIDriver.checkMod(user) or user == "aphiremarbl"):
                            list = msg.split(" ")
                            type = list[1]
                            command.startBet(s, type)
                            currentBetting = True
                            paid = False
                        else:
                            command.chat(s, "You do not have permission!")
                    elif ("!help") in msg:
                        command.chat(s,"More features coming! nosaltbot is in beta!")
                        command.chat(s,"Commands: !coins, !bet")
                    # elif ("!sr") in msg:
                    #     list = msg.split(" ")
                    #     link = list[1]


                if currentBetting:
                    if not timer.betTimer():
                        currentBetting = False
                        command.chat(s,"Betting has closed")
                        #bets.percentages()

                if not paid and not currentBetting:
                    op1 = op2 =op3=op4=op5=""
                    file = open("vars.txt",'r')
                    outcome = file.read()
                    file.close()
                    #print(outcome)
                    if int(type) == 1:
                        op1 = "Win"
                        op2 = "Lose"
                    elif int(type) == 2:
                        op1 = "1st place"
                        op2 = "2nd place"
                        op3 = "3rd place"
                        op4 = "Lose"

                    if outcome == "1":
                        command.stateWinners(s,BETOPONE)
                        bets.payoutsOne(type)
                        command.chat(s,"Bets on "+op1+" have been paid out. Enjoy!")
                        paid = True
                    elif outcome == "2":
                        command.stateWinners(s, BETOPTWO)
                        bets.payoutsTwo(type)
                        command.chat(s, "Bets on "+op2+" have been paid out. Enjoy!")
                        paid = True
                    elif outcome == "3":
                        command.stateWinners(s, BETOPTHREE)
                        bets.payoutsThree(type)
                        command.chat(s, "Bets on " + op3 + " have been paid out. Enjoy!")
                        paid = True
                    elif outcome == "4":
                        command.stateWinners(s, BETOPFOUR)
                        bets.payoutsFour(type)
                        command.chat(s, "Bets on " + op4 + " have been paid out. Enjoy!")
                        paid = True
                    elif outcome == "5":
                        command.stateWinners(s, BETOPFIVE)
                        bets.payoutsFive(type)
                        command.chat(s, "Bets on " + op5 + " have been paid out. Enjoy!")
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