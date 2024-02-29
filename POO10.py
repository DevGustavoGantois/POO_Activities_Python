#Crie uma interface chamada"Veículo"com métodos "acelerar"
#e"frear." Em seguida, crie classes concretas como"Carro
#"e"Bicicleta"que implementem a interface "Veículo"
#e forneçam suas próprias implementações dos métodos"acelerar"
#e"frear." Demonstre como o
#polimorfismo pode ser usado para tratar diferentes tipos
#de veículos de maneira uniforme, chamando os métodos
#da interface

from abc import ABC, abstractmethod

#Definir a interface do veículo
class Vehicle(ABC):
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

#Implementação da classe Carro que herda de Veículo:

class Car(Vehicle):
    def accelerate(self):
        print("Accelerating Car!")

    def brake(self):
        print("Braking Car.")

#Implementando da classe Bicicleta que herda de Veículo:
class Bicycle(Vehicle):
    def accelerate(self):
        print('bicycle pedaling faster!')
    
    def brake(self):
        print("Braking bicycle.")

#Usando polimorfismo:
def using_vehicle(vehicle):
    vehicle.accelerate()
    vehicle.brake()

#Exemplo do uso do polimorfismo:
car = Car()
bicycle = Bicycle()

using_vehicle(car)
using_vehicle(bicycle)


def main():
    while True:
        print("CARS AND BICYCLES")
        print("<=====================>")
        print("Type '1'- Speed up the car.")
        print("Type '2'- Brake the car.")
        print("Type '3'- Speed the Bicycle.")
        print("Type '4'- Brake the Bicycle.")
        print("Type '5' - Exit the program.")
        print("<=========================>")

        option = int(input("Enter a option:"))

        if option == 1:
            car = Car()
            car.accelerate()
        elif option == 2:
            car = Car()
            car.brake()
        elif option == 3:
            bicycle = Bicycle()
            bicycle.accelerate()
        elif option == 4:
            bicycle = Bicycle()
            bicycle.brake()
        elif option == 5:
            print("Finished the program.")
            break
        else:
            ValueError("Invalid number. Choose of 1-5.")

if __name__ == '__main__':
    main()
