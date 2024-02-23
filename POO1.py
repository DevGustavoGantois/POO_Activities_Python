#Crie um classe chamada cachorro com os atributos: nome, raça, idade

class Cachorro:
    def __init__(self, nome, raca, idade, latir):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.latir = latir

    def Caracteristicas_cachorro(self):
        print(f"O nome do cachorro é {self.nome} e a raça dele é {self.raca}. Ele tem {self.idade} anos... e faz {self.latir}")

meu_cachorro = Cachorro('Frederico', 'Bulldog Inglês', 3, 'AuAu')

meu_cachorro.Caracteristicas_cachorro()


