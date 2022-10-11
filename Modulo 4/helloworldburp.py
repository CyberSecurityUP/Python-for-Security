# Todas as extensões devem implementar esta interface.
# As implementações devem ser chamadas de BurpExtender, no pacote burp, devem ser declaradas públicas e devem fornecer um construtor padrão (público, sem argumentos).
from burp import IBurpExtender
# Ele é usado para imprimir a representação formatada de objetos no fluxo de saída de texto.
from java.io import PrintWriter
# Uma classe especifica para usar excessões
from java.lang import RuntimeException

class BurpExtender(IBurpExtender):
    
    #
    # implementando a classe IBurpExtender
    #
    
    def	registerExtenderCallbacks(self, callbacks):
        # Este método é usado quando a extensão é carregada
        
        # defina o nome da extensão
        callbacks.setExtensionName("Hello world extension")
        
        # Obter o fluxo de saida de erros
        stdout = PrintWriter(callbacks.getStdout(), True)
        stderr = PrintWriter(callbacks.getStderr(), True)
        
        # Escreva a mensagem no fluxo de output
        stdout.println("Hello output")
        
        # Escreva uma mensagem caso aconteça algum erro
        stderr.println("Hello errors")
        
        # escreva uma mensagem na guia de alertas do Burp
        callbacks.issueAlert("Hello alerts")
        
        # lançar uma exceção que aparecerá em nosso fluxo de erro
        raise RuntimeException("Hello exception")
