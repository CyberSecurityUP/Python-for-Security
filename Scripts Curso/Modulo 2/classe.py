class animal:
    atributo1 = "papagaio"
    atributo2 = "cachorro"

    def funcao(self):
        print("Esse animal é", self.atributo1)
        print("Esse animal é", self.atributo2)
        
nomeanimal = animal()

print(nomeanimal.atributo2)
