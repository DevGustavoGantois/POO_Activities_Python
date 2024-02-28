#Crie uma hierarquia de classes que represente veículos.Comece com uma classe base
#"Veículo"e, em seguida,crie classes derivadas como
#"Carro"e"Bicicleta." Adicione métodos para definir atributos, como
#"cor"e"modelo,"e permita a chamada de métodos em cadeia para configurar esses atributos

class Vehicle:
    def __init__(self, color=None, model=None, vehicle_type=None):
        self.color = color
        self.model = model
        self.vehicle_type = vehicle_type

    def set_characteristics(self, color, model, vehicle_type):
        self.color = color
        self.model = model
        self.vehicle_type = vehicle_type
        return self
    
class Car(Vehicle):
    def set_characteristics(self):
        return super().set_characteristics('Red', 'Ferrari', 'Car')
    
class Bicycle(Vehicle):
    def set_characteristics(self):
        return super().set_characteristics('Black', 'Trek', 'Bicycle')
    
class Bus(Vehicle):
    def set_characteristics(self): 
        return super().set_characteristics('Yellow', 'Mercedes-Benz', 'Bus')
    
class Motorcycle(Vehicle):
    def set_characteristics(self):
        return super().set_characteristics('Blue', 'Ducati 1200', 'Motorcycle')
    
#Instanciando as classes:
car = Car().set_characteristics()
bicycle = Bicycle().set_characteristics()
bus = Bus().set_characteristics()
motorcycle = Motorcycle().set_characteristics()

print("The Vehicle is:")
print(f"Type: {car.vehicle_type}.")
print(f"Model: {car.model}.")
print(f"Color: {car.color}.")
print("<========================>")
print(f"Type:{bicycle.vehicle_type}.")
print(f"Model:{bicycle.model}.")
print(f"Color:{bicycle.color}.")
print("<==========================>")
print(f"Type:{bus.vehicle_type}.")
print(f"Model:{bus.model}")
print(f"Color:{bus.color}")
print("<============================>")
print(f"Type:{motorcycle.vehicle_type}.")
print(f"Model:{motorcycle.model}.")
print(f"Color:{motorcycle.color}.")
