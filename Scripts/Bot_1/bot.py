from .config import *

class Bot(object):
    def __init__(self):
        self.var = 0

    def chat(self,sock,msg):
        """
           Send a chat message to the server.
           Keyword arguments:
           sock -- the socket over which to send the message
           msg  -- the message to be sent
           """
        sock.send("PRIVMSG #{} :{}".format(CHAN, msg))

    def ban(self,sock,user):
        """
            Ban a user from the current channel.
            Keyword arguments:
            sock -- the socket over which to send the ban command
            user -- the user to be banned
            """
        self.chat(sock,".ban {}".format(user))

    def timeout(self,sock,user,secs=600):
        """
           Time out a user for a set period of time.
           Keyword arguments:
           sock -- the socket over which to send the timeout command
           user -- the user to be timed out
           secs -- the length of the timeout in seconds (default 600)
           """
        self.chat(sock, ".timeout {}".format(user,secs))