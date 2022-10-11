# Todas as extensões devem implementar esta interface.
# As implementações devem ser chamadas de BurpExtender, no pacote burp, devem ser declaradas públicas e devem fornecer um construtor padrão (público, sem argumentos).
from burp import IBurpExtender


class BurpExtender(IBurpExtender):

    #implementando a classe IBurpExtender
    
    def registerExtenderCallbacks(self,callbacks):
        # Este método é usado quando a extensão é carregada
        callbacks.setExtensionName("Hello World2")
        # Nome da extensão
        for x in xrange(1,100):
            # Criei um loop que vai printar hello de 0 a 100
            string = "hello " + str(x)
            callbacks.printOutput(string)
        return
