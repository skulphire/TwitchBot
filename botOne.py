from Scripts.Bot_1 import bot
from Scripts.Bot_1.config import *
from Scripts.Bot_1 import threads
from Scripts.Bot_1 import saltcoins
import socket
import time
import re
import threading


if __name__ == '__main__':
    s = socket.socket()
    coins = saltcoins.Coins()

    followers = input("How many followers? ")
    try:
        s.connect((HOST,PORT))
    except Exception:
        s.connect((HOST,WEB_PORT))

    s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

    command = bot.Bot()
    threader = threads.Threads()
    threader.getAllFollowers(followers)

    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0) # return the entire match
            message = bot.CHAT_MSG.sub("", response)
            #print(username + ": " + message)

            minuteCoins = threading.Timer(10, coins.timedCoins())
            if not minuteCoins.isAlive():
                print("Starting minuteCoins...")
                minuteCoins.start()



            #if "!bet" in message:
            #    list = message.split(" ")
            #    amount = list[1]
            #    option = list[2]

        time.sleep(1/RATE)

