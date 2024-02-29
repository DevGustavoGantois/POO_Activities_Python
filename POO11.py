#Crie uma classe base chamada"Animal"com um método 
#"emitirSom." Em seguida, crie classes derivadas como
#"Cachorro," "Gato" e "Pássaro"que herdem de"Animal"
#e sobrescrevam o método"emitirSom"para cada tipo de animal.
#Crie uma lista de animais e percorra-a, chamando o método"emitirSom"
#para cada animal. Demonstre como o polimorfismo
#permite que diferentes tipos de animais emitam seus sons de maneira uniforme.

class Animal:
    pass
class dog(Animal):
    def __init__(self):
        self.sound = 'AuAuAuAu'
    #As funções tem o mesmo nome pois elas executam a mesma coisa, dependendo da escolha o som será diferente.
    def make_sound(self):
        print(self.sound)
    
class cat(Animal):
    def __init__(self):
        self.sound = 'MeowMeowMeow'

    def make_sound(self):
        print(self.sound)
    
class bird(Animal):
    def __init__(self):
        self.sound = 'PipiuPiuPiu'
    def make_sound(self):
        print(self.sound)


def make_sounds_animals(animal_list):
    for animal in animal_list:
        animal.make_sound()

if __name__ == '__main__':
    #Criando a lista com cada animal dentro dela.
    animal_list = [dog(), cat(), bird()]
    
    while True:
        print("SOUNDS OF ANIMALS")
        print("<====================>")
        print("Type '1' - Sound of Dog.")
        print("Type '2' - Sound of Cat.")
        print("Type '3' - Sound of Bird.")
        print("Type '4' - Finished the program.")
        print("<============================>")
        
        option = int(input("Enter a option:"))

        if option == 1:
            make_sounds_animals([dog()])
        elif option == 2:
            make_sounds_animals([cat()])
        elif option == 3:
            make_sounds_animals([bird()])
        elif option == 4:
            print("Finished Program.")
            break
        else:
            ValueError("Choose Option 1-4")