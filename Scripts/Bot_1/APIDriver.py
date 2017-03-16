from .config import *
from .TwitchAPI import API
import json

class APIDriver(object):
    def __init__(self):
        self.api = API()

    def getNewFollowers(self, limit=25, direction='desc'):
        newsy = []
        followers = self.api.getFollowers(limit,direction)
        followers = json.loads(followers)
        for follower in followers['follows']:
            #print(follower['user']['display_name'])
            newsy.append(follower['user']['display_name'])
        for count in range(0,limit):
            if not newsy[count] == ALLFOLLOWERS[count]:
                NEWFOLLOWERS.append(newsy[count])

    def getAllFollowers(self, limit, direction='desc'):
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
            CURRENTVIEWERS.append(viewer)