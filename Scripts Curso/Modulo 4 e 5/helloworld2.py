# -*- coding: utf-8 -*-
from burp import IBurpExtender
from java.io import PrintWriter
from java.lang import RuntimeException

class BurpExtender(IBurpExtender):

    def registerExtenderCallbacks(self, callbacks):

        callbacks.setExtensionName("Hello World 2")

        for x in xrange(1,100):
            string = "hello " + str(x)
            callbacks.printOutput(string)
        return
