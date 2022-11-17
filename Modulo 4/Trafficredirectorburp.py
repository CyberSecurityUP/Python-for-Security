# -*- coding: utf-8 -*-

#Biblioteca da API
from burp import IBurpExtender
# Biblioteca para fazer comunicação HTTP
from burp import IHttpListener
from java.io import PrintWriter

# definir o host de origem
HOST_FROM = "127.0.0.1"
# definir o host de destino
HOST_TO = "www.google.com"

#Criando duas funçõe com o nomes das bibliotecas para implementa-las
class BurpExtender(IBurpExtender, IHttpListener):

    #
    # implement IBurpExtender 
    #
    
    def	registerExtenderCallbacks(self, callbacks):
        # obter um objeto auxiliar de extensão
        self._helpers = callbacks.getHelpers()
        
        # definir o nome da extensão
        callbacks.setExtensionName("Traffic redirector")

        # habilitar o modo Debuger para coletar erros o stdout coleta entrada e saida de erros
        self.stdout = PrintWriter(callbacks.getStdout(), True);
        self.stdout.println("DEBUG: Habilitado!")
        
        # Crieum ouvinte HTTP
        callbacks.registerHttpListener(self)

    #
    # implementando o IHttpListener
    #
    
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        # Ele mostra no debug o processamento das solicitações        
        self.stdout.println("DEBUG: Entrando na funcao processHttpMessage") 
        # apenas processar solicitações
        if not messageIsRequest:
            self.stdout.println("Debug: Essa mensagem não é uma requisicao, parando processo")
            return

        # obter o serviço HTTP para a solicitação e trazer informações
        httpService = messageInfo.getHttpService()
        self.stdout.print("Debug: httpservice ")
        self.stdout.println(httpService)
        self.stdout.print("Debug: httpservice.gethost() ")
        self.stdout.println(httpService.getHost())
        self.stdout.print("Debug: HOST_TO")
        self.stdout.println(HOST_TO)
        self.stdout.print("Debug: HOST_FROM ")
        self.stdout.println(HOST_FROM)
        
        # se o host for HOST_FROM, mude para HOST_TO, ele vai usar o iHTTPListener para fazer o redirecionamento, abaixo vamos configurar todo processo
        if (HOST_FROM == httpService.getHost()):
            self.stdout.println("Debug: HOST_TO and HOST_FROM são o mesmo servidor")
            # construindo um listener http e fazendo o redirect
            messageInfo.setHttpService(self._helpers.buildHttpService(HOST_TO,
                httpService.getPort(), httpService.getProtocol()))
            self.stdout.println("Debug: Se o for HOST_FROM, mude para o HOST_TO ")
            self.stdout.println(httpService)
