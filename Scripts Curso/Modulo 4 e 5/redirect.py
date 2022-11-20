# -*- coding: utf-8 -*-

from burp import IBurpExtender

from burp import IHttpListener
from java.io import PrintWriter

HOST_FROM = "10.0.0.139"

HOST_TO = "www.pudim.com.br"

class BurpExtender(IBurpExtender, IHttpListener):

    def registerExtenderCallbacks(self, callbacks):
        self._helpers = callbacks.getHelpers()

        callbacks.setExtensionName("Redirect")

        self.stdout = PrintWriter(callbacks.getStdout(), True)
        self.stdout.println("Debug esta habilitado")

        callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):

        self.stdout.println("Debug: Ele esta entrando na funcao processHttpMessage")

        if not messageIsRequest:
            self.stdout.println("Debug: Isso não é uma requisicao valida")
            return

        httpService = messageInfo.getHttpService()
        self.stdout.print("Debug: Entrando no httpservice")
        self.stdout.println(httpService)
        self.stdout.print("Debug: Entrando no httpservice.gethost()")
        self.stdout.println(httpService.getHost())
        self.stdout.print("Debug: Entrando na HOST_TO")
        self.stdout.println(HOST_TO)
        self.stdout.print("Debug: Entrando no HOST_FROM")
        self.stdout.println(HOST_FROM)

        if(HOST_FROM == httpService.getHost()):
            self.stdout.println("Debug: HOST_TO e HOST_FROM são os mesmos IPs")
            messageInfo.setHttpService(self._helpers.buildHttpService(HOST_TO, httpService.getPort(), httpService.getProtocol()))
            self.stdout.println("Debug: Se o HOST_FROM for diferente mude para o HOST_TO")
            self.stdout.println(httpService)
    
