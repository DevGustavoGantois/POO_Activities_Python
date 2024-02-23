#Crie um classe chamada pessoa com os atributos: nome,idade, peso, gênero

class People:
    def __init__(self, name, age, weight, gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender

    def people_speak(self):

        print(f"Hi my name is: {self.name} i´m {self.age} and my weight {self.weight}, my gender is: {self.gender}.")

    def information_people(self):

        print(f"Name:{self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}kg")
        print(f"Gender: {self.gender}")

gustavo = People('Gustavo', 20, 84.5, 'Hétero')

gustavo.people_speak()
gustavo.information_people()