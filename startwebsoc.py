#!/usr/bin/env python
# -*- coding: utf-8 -*
from twisted.internet import reactor
from autobahn.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol, \
    listenWS
import scripts.callSentenceGenClass
import scripts.settingloader
import codecs


class EchoServerProtocol(WebSocketServerProtocol):
    def __init__(self):
        settings=scripts.settingloader.loadsettings("settings.json")
        self.csgc=scripts.callSentenceGenClass.callSentenceGenClass(settings['modelname'])

def onOpen(self):
    print "Connect"

    def onMessage(self, msg, binary):
        print msg
        print binary
        if(msg.find("出雲")!=-1):
            self.sendMessage("護衛艦です")
        else:
            decodedmsg=msg.decode('utf-8')
            rawsentence=self.csgc.callSentenceGen_pickle(decodedmsg)
            print type(rawsentence)
            returnmsg="".join(rawsentence).encode('utf-8')
            self.sendMessage(returnmsg)

if __name__ == '__main__':

    factory = WebSocketServerFactory("ws://localhost:9000", debug = False)
    factory.protocol = EchoServerProtocol
    listenWS(factory)
    reactor.run()
