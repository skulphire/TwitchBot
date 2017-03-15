from .config import *
from .TwitchAPI import API
import json

class Threads(object):
    def __init__(self):
        self.api = API()

    def updateFollowers(self,limit=25,direction='desc'):
        followers = self.api.getFollowers(limit,direction)
        followers = json.loads(followers)
        for follower in followers['follows']:
            #print(follower['user']['display_name'])
            CURRENTVIEWERS.append(follower['user']['display_name'])

    def getAllFollowers(self, limit, direction='desc'):
        followers = self.api.getFollowers(limit, direction)
        followers = json.loads(followers)
        for follower in followers['follows']:
            ALLFOLLOWERS.append(follower['user']['display_name'])

    def updateViewers(self, group):
        viewers = self.api.getViewers()
        viewers = json.loads(viewers)
        for viewer in viewers['chatters'][group]:
            #print(viewer)
            CURRENTVIEWERS.append(viewer)