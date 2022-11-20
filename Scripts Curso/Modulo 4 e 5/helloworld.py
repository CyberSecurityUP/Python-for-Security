# -*- coding: utf-8 -*-
from burp import IBurpExtender
from java.io import PrintWriter
from java.lang import RuntimeException

class BurpExtender(IBurpExtender):

    def registerExtenderCallbacks(self, callbacks):

        callbacks.setExtensionName("Hello World")

        stdout = PrintWriter(callbacks.getStdout(), True)
        stderr = PrintWriter(callbacks.getStderr(), True)

        stdout.println("Aconteceu uma saida")

        stderr.println("Aconteceu um erro")

        callbacks.issueAlert("Alertas acontecendo")

        raise RuntimeException("Aconteceu uma excessão")
