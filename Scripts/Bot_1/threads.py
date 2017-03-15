from .config import *
from .TwitchAPI import API
import json

class Threads(object):
    def __init__(self):
        self.api = API()

    def updateFollowers(self,limit=25,direction='desc'):
        followers = self.api.getFollowers(limit,direction)
        followers = json.loads(followers)
        for follower in followers['follow']:
            print(follower['user']['display_name'])