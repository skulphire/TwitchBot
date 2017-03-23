from .config import *
from .TwitchAPI import API
import json

class APIDriver(object):
    def __init__(self):
        self.api = API()

    def getNewFollowers(self, limit=25, direction='desc'):
        newsy = []
        check = False
        followers = self.api.getFollowers(limit,direction)
        followers = json.loads(followers)
        for follower in followers['follows']:
            #print(follower['user']['display_name'])
            newsy.append(follower['user']['display_name'])

        for count in range(0,limit):
            if not newsy[count] in ALLFOLLOWERS:
                NEWFOLLOWERS.append(newsy[count])
                check = True
        return check

    def addNewToAll(self):
        for index in range(0,len(NEWFOLLOWERS)):
            ALLFOLLOWERS.append(NEWFOLLOWERS[index])

    def getAllFollowers(self, limit, direction='asc'):
        followers = self.api.getFollowers(limit, direction)
        followers = json.loads(followers)
        for follower in followers['follows']:
            #print(follower['user']['display_name'])
            ALLFOLLOWERS.append(follower['user']['display_name'])

    def updateViewers(self, group):
        viewers = self.api.getViewers()
        viewers = json.loads(viewers)
        for viewer in viewers['chatters'][group]:
            #print(viewer)
            if not viewer in CURRENTVIEWERS:
                CURRENTVIEWERS.append(viewer)
                if not viewer in USERCOINS:
                    USERCOINS[viewer] = DEFAULTCOIN

    def checkMod(self, user):
        viewers = self.api.getViewers()
        viewers = json.loads(viewers)
        if user in viewers['chatters'][MOD]:
            return True
        else:
            return False