from .config import *
import requests

class API(object):
    def __init__(self):
        self.rootAPI = "https://api.twitch.tv/kraken/"

    def getFollowers(self,limit=25,direction='desc'):
        url = self.rootAPI+"channels/aphiremarbl/follows"
        queryString = "?limit=%s&direction=%s" % (limit, direction)

        headers = {
            'Client-ID': CLIENT_ID
        }
        req = requests.get(url+queryString,headers=headers)
        return req.text

    def getViewers(self):
        url = "https://tmi.twitch.tv/group/user/aphiremarbl/chatters"
        queryString = ""
        req = requests.request('GET', url+queryString)
        return req.text