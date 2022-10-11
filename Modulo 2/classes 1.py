#Ele é executado assim que um objeto de uma classe é instanciado. O método é útil para fazer
#qualquer inicialização que você queira fazer com seu objeto.
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome
# O Self referencia atributo de uma instância

joas = Pessoa('Joas')
print(joas)
michael = Pessoa('Michael')
print(michael)
lucas = Pessoa('Lucas')
print(lucas)

class Dog:
 
    # A simple class
    # Vamos criar dois atributos com nome dos cachorro
    attr1 = "spike"
    attr2 = "bob"
 
    # Usar um simples método para referenciar os atributos
    def fun(self):
        print("Eu sou", self.attr1)
        print("Eu sou", self.attr2)
 
 
# Variavel com nome cachorro, passando
# o objeto Dog
namedog = Dog()
 
# Acessando atributos de classe
# e método através de objetos, passando a função fun com o objeto Dog
print(namedog.attr1)
print(namedog.attr2)
namedog.fun()
