#Exercícios de revisão sobre POO
#Crie uma hierarquia de classes representando formas
#geométricas. Comece com uma classe base chamada "Forma"
#e, em seguida, crie classes derivadas como "Círculo"e"Retângulo"que herdem da classe base.
#Adicione métodos para calcular área e perímetro em cada classe derivada.
import math

class Shape:
    def __init__(self):
        self.area = 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()

    def calculate_area(self):
        area = math.pi * self.radius**2
        return area
    
    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        super().__init__()

    def calculate_area(self):
        area = self.base * self.height
        return area
    
    def calculate_perimeter(self):
        perimeter = 2 * (self.base + self.height)
        return perimeter
    
class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def calculate_area(self):
        area = self.side**2
        return area
    
    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter
    
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def calculate_area(self):
        area = (self.base * self.height) / 2
        return area
    
    def calculate_perimeter(self):
        hypotenuse = math.sqrt(self.base**2 + self.height**2)
        perimeter = self.base + self.height + hypotenuse
        return perimeter

def main():
    while True:
        print("CALCULATION PERIMETER")
        print('''<------------------------------------------------------------>
            Type (1) Show the area and perimeter of Circle.
            Type (2) Show the area and perimeter of Rectangle.
            Type (3) Show the area and perimeter of Square.
            Type (4) Show the area and perimeter of Triangle.
            Type (5) Exit the program.
            <---------------------------------------------------------------------->''')
        
        option = int(input("Enter an option: "))

        # Instantiate all classes now.
        if option == 1:
            radius = float(input("Enter the radius of Circle: "))
            circle = Circle(radius)
            print(f'Area of Circle: {circle.calculate_area()}')
            print(f'Perimeter of Circle: {circle.calculate_perimeter()}')
        elif option == 2:
            base = float(input("Enter the base of rectangle: "))
            height = float(input("Enter the height of rectangle: "))
            rectangle = Rectangle(base, height)
            print(f'Area of Rectangle: {rectangle.calculate_area()}')
            print(f'Perimeter of Rectangle: {rectangle.calculate_perimeter()}')
        elif option == 3:
            side = float(input("Enter the side of Square: "))
            square = Square(side)
            print(f'Area of Square: {square.calculate_area()}')
            print(f'Perimeter of Square: {square.calculate_perimeter()}')
        elif option == 4:
            base = float(input("Enter the base of triangle: "))
            height = float(input("Enter the height of triangle: "))
            triangle = Triangle(base, height)
            print(f'Area of Triangle: {triangle.calculate_area()}')
            print(f'Perimeter of Triangle: {triangle.calculate_perimeter()}')
        elif option == 5:
            print("Finished the program.")
            break
        else:
            raise ValueError("Invalid option, Choose option 1-5.")

if __name__ =="__main__":
    main()


#Crie uma hierarquia de classes que represente veículos.
#Comece com uma classe base "Veículo "e, em seguida,
#crie classes derivadas como "Carro"e" Bicicleta." Adicione
#métodos para definir atributos, como "cor" e
#"modelo, "e permita a chamada de métodos em cadeia para configurar esses atributos.    

class Vehicle:
    def __init__(self, model= '', color= '', sound= ''):
        self.model = model
        self.color = color
        self.sound = sound
class Car(Vehicle):
    def car1(self):
        self.model = 'BMW'
        self.color = 'Black'
        self.sound = 'VRUM VRUM VRUM'
        return f'Type of Car 1: Model-{self.model}, Color-{self.color}, Sound-{self.sound}.'
    def car2(self):
        self.model = 'Ferrari'
        self.color = 'Red'
        self.sound = 'VRUM VRUM VRUM'
        return f'Type of Car 2: Model-{self.model}, Color-{self.color},Sound-{self.sound}.'
    def car3(self):
        self.model = 'Toyota'
        self.color = 'Blue'
        self.sound = 'Blue'
        return f'Type of Car 3: Model-{self.model}, Color-{self.color}, Sound-{self.sound}.' #Retornando os métodos 
class Bicycle(Vehicle):
    def Bicycle1(self):
        self.model = 'Caloi'
        self.color = 'brown'
        self.sound = 'plim plim plim'
        return f'Type of Bicycle 1: Model-{self.model}, Color-{self.color}, Sound-{self.sound}.'
    def Bicycle2(self):
        self.model = 'Cannondale'
        self.color = 'green'
        self.sound = 'plim plim plim'
        return f'Type of Bicycle 2: Model-{self.model}, Color-{self.color}, Sound-{self.sound}.'
    def bicycle3(self):
        self.model = 'Giant'
        self.color = 'orange'
        self.sound = 'plim plim plim'
        return f'Type of Bicycle 3: Model-{self.model}, Color-{self.color}, Sound-{self.sound}.'

def main_program():
    while True:
        print('''MODEL OF VEHICLES
          <------------------------------------------->
          Type (1) Show the types of Car.
          Type (2) Show the types of Bicycle. 
          Type (0) Exit the program.
          <--------------------------------------------->''')
        option = int(input("Enter a option:"))
        if option == 1:
            car = Car()
            type_car = int(input("Enter the type of car [1,2,3]:"))
            if type_car == 1: 
                print(car.car1())
            elif type_car == 2:
                print(car.car2())
            elif type_car == 3:
                print(car.car3())
            else:
                ValueError("THE OPTION IS NOT EXIST.")
        elif option == 2:
            bicycle = Bicycle()
            type_bicycle = int(input("Enter the type of bicycle [1,2,3]:"))
            if type_bicycle == 1:
                print(bicycle.Bicycle1())
            elif type_bicycle == 2:
                print(bicycle.Bicycle2()) #Mostrando os métodos de acordo com as escolhas dentro das opções dadas
            elif type_bicycle == 3:
                print(bicycle.bicycle3())
            else:
                ValueError("THE OPTION IS NOT EXIST.")
        elif option == 0:
            print("The program is finished.")
            break
        else:
            ValueError("THE OPTION IS NOT EXIST.") 

if __name__ == "__main__":
    main_program()

#Crie uma classe chamada "Calculadora" com um método "somar" que pode somar dois números inteiros ou duas strings. 
#Use o polimorfismo para implementar a
#sobrecarga do método"somar"para que ele funcione com diferentes tipos de entrada (números inteiros e
#strings). Crie exemplos de uso para demonstrar como a mesma função pode se comportar de maneira diferente com base nos tipos de entrada.
    
class Calculator:
    def sum_numbers_and_letters(self, num1, num2, string1, string2):
        if isinstance(num1, int) and isinstance(num2, int):
            return num1 + num2
        elif isinstance (string1, str) and isinstance (string2, str):
            return string1 + string2
        else:
            raise ValueError("Invalid option...")

def main1():
    calculator = Calculator()
    while True:
        print('''CALCULATOR NUMBERS AND CONCAT STRINGS.
              <------------------------------------------------------------>
              Type (1) Calculation sum numbers.
              Type (2) Concat strings.
              Type (3) Exit the program.
              <------------------------------------------------------------->''')
        option = int(input("Enter a option:"))
        if option == 1:
            number1 = int(input("Enter a number 1:"))
            number2 = int(input("Enter a number 2:"))
            result = calculator.sum_numbers_and_letters(num1=number1, num2=number2, string1=None, string2=None)
            print(f"Result: {result}.")
        elif option  == 2:
            string1 = str(input("Enter a string 1:"))
            string2 = str(input("Enter a string 2:"))
            result = calculator.sum_numbers_and_letters(num1=None, num2=None, string1=string1, string2=string2)
            print(f"Result: {result}.")
        elif option == 3:
            print("Exit program.")
            break
        else:
            print("The option is not exist.")

if __name__ == "__main__":
    main1()

#Crie uma interface chamada "Veículo"com métodos "acelerar"e "frear." Em seguida, crie classes concretas
#como"Carro"e"Bicicleta"que implementem a interface "Veículo"e forneçam suas próprias implementações dos 
#métodos "acelerar" e "frear." Demonstre como o polimorfismo pode ser usado para tratar diferentes tipos
#de veículos de maneira uniforme, chamando os métodos da interface.
from abc import ABC, abstractmethod

class Vehicle:
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def brake(self):
        pass
        
class Car(Vehicle):
    def accelerate_vehicle(self):
        return 'Acelerating Car.'
    def brake_vehicle(self):
        return 'Braking Car.'
class Bicycle(Vehicle):
    def accelerate_vehicle(self):
        return 'Acelerating Bicycle.'
    def brake_vehicle(self):
        return 'Braking Bicycle.'

def main_program1():
    while True:
        print('''COMMAND LIST VEHICLE
            <------------------------------------->
            Type (1) Commands Car
            acelerate
            brake
            ... 
            Type (2) Commands Bicycle 
            acelerate
            brake
            ...
            Type (3) Exit the program
            <---------------------------------------->''')
        option = int(input('Enter a option:'))
        if option == 1:
            car = Car()
            accelerate_or_brake = input("Do you want accelerate car or brake car [accelerate/brake]:")
            if accelerate_or_brake.lower() == 'accelerate':
                result = car.accelerate_vehicle() 
                print(result)
                #talvez dê erro, qualquer coisa eu boto a classe Car para testar.
            elif accelerate_or_brake.lower() == 'brake':
                result = car.brake_vehicle()
                print(result)
        elif option == 2:
            bicycle = Bicycle()
            accelerate_or_brake = input("Do you want accelerate bicycle or brake bicycle [accelerate/brake]:")
            if accelerate_or_brake.lower() == 'accelerate':
                result = bicycle.accelerate_vehicle() 
                print(result)
                #talvez dê erro, qualquer coisa eu boto a classe Bicycle para testar.
            elif accelerate_or_brake.lower() == 'brake':
                result = bicycle.brake_vehicle()
                print(result)   
        elif option == 3:
            print("Finished Program.")
            break
        else:
            raise ValueError("Try Again. Choose a option [1-3]")
        
if __name__ == '__main__':
    main_program1()

#Crie uma classe base chamada "Animal" com um método" emitirSom." Em seguida, crie classes derivadas como "Cachorro," " Gato "e" Pássaro "
#que herdem de
#"Animal"e sobrescrevam o método "emitirSom "para cada tipo de animal. Crie uma lista de animais e percorra-a, chamando o método "emitirSom
#"para cada animal. Demonstre como o polimorfismo permite que diferentes tipos de animais emitam seus sons de maneira uniforme.

class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    def sound_animals(self):
        return 'Au Au Au'
class Cat(Animal):
    def sound_animals(self):
        return 'Meow Meow Meow'
class Bird(Animal):
    def sound_animals(self):
        return 'Piu Piu Piu Piu.'

def program_main():
    animals = [Dog(), Cat(), Bird()]

    for animal in animals:
        sound = animal.sound_animals()
        print(f"The sound of {animal.__class__.__name__}: {sound}.")

if __name__ == '__main__':
    program_main()

#sistema de gerenciamento de contas bancárias em Python
    
#Crie um sistema de gerenciamento de contas bancárias
#em Python usando herança e polimorfismo. O sistema
#deve incluir as seguintes classes:

#Classe ContaCorrente:
#-A classe
#"ContaCorrente" herda de"Conta" e inclui atributos específicos, como taxa de manutenção e limite de cheque especial.
#-Deve sobrescrever o método de saque para
#considerar o limite de cheque especial, se
#necessário.

#Classe ContaPoupanca:
#-A classe
#"ContaPoupanca" também herda de "Conta" e inclui atributos específicos, como taxa de juros.
#-Ela deve ter um método para calcular e adicionar juros ao saldo. Polimorfismo:
#-Crie um método chamado resumo que pode ser chamado
#em qualquer objeto de conta (ContaCorrente ou ContaPoupanca).

#Esse método resumo irá exibir um resumo das
#informações da conta, incluindo o tipo de conta (corrente ou poupança), o número da conta, o
#titular da conta e o saldo atual. Teste de Funcionalidade:
#Crie um programa principal que demonstre o uso dessas classes. Crie instâncias de contas
#correntes e poupanças, realize depósitos, saques, adicione juros e chame o método resumo para cada conta.
    
class Account:
    def __init__(self, account_holder, account_type, account_number, balance):
        self.account_holder = account_holder
        self.account_type = account_type
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful.")
        else:
            print("Insufficient balance.")

    def summary(self):
        print(f"Account Type: {self.account_type}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


class CheckingAccount(Account):
    def __init__(self, account_holder, account_number, balance, maintenance_fee, overdraft_limit):
        super().__init__(account_holder, "Checking", account_number, balance)
        self.maintenance_fee = maintenance_fee
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful.")
        else:
            print("Overdraft limit exceeded.")


class SavingsAccount(Account):
    def __init__(self, account_holder, account_number, balance, interest_rate):
        super().__init__(account_holder, "Savings", account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance *= (1 + self.interest_rate / 100)


def program_main2():
    checking_account = CheckingAccount("Gustavo", "5678910", 1000, 20, 500)
    savings_account = SavingsAccount("Matheus", "112233", 3000, 8)

    print("Deposit into the checking account.")
    checking_account.deposit(5000)

    print("\nWithdrawal from the checking account.")
    checking_account.withdraw(1000)

    print("\nWithdrawal with overdraft limit from the checking account.")
    checking_account.withdraw(2450)

    print("\nDeposit into the savings account.")
    savings_account.deposit(1500)

    print("\nAdd interest to the savings account.")
    savings_account.add_interest()

    print("\nChecking account summary:")
    checking_account.summary()

    print("\nSavings account summary:")
    savings_account.summary()


if __name__ == "__main__":
    program_main2()

#A classe principal será chamada de "Material" e terá um construtor que recebe dois parâmetros: 
#"titulo" e "autor_ou_editora". Essa classe também terá um método chamado "exibir_informacoes"  
#que imprimirá na saída o título e o autor/editora do material.
#A classe "Livro" será uma subclasse da classe "Material" e terá um construtor que recebe três parâmetros: 
#"titulo", "autor_ou_editora" e "genero". Essa classe também terá um método "exibir_informacoes" que chamará o método correspondente 
#na classe "Material" e imprimirá o gênero do livro.
#A classe "Revista" será outra subclasse da classe "Material" e terá um construtor que recebe três parâmetros: 
#"titulo", "autor_ou_editora" e "edicao". Essa classe também terá um método "exibir_informacoes" que chamará o método correspondente na 
#classe "Material" e imprimirá a edição da revista.
#Crie instâncias das classes "Livro" e "Revista" com informações específicas e chame o método "exibir_informacoes" 
#para mostrar os detalhes de cada material
    
class Material:
    def __init__(self, title, author_or_publisher):
        self.title = title
        self.author_or_publisher = author_or_publisher
    def display_informations(self):
        print(f'''Material Title: {self.title}.
Athor or Publisher: {self.author_or_publisher}.''')
        
class Book(Material):
    def __init__(self, title, author_or_publisher, genre):
        super().__init__(title, author_or_publisher)
        self.genre = genre

    def display_informations(self):
        super().display_informations()
        print(f"Genre of Book: {self.genre}")

class Magazine(Material):
    def __init__(self, title, author_or_publisher, edition):
        self.title = title
        self.author_or_publisher = author_or_publisher
        self.edition = edition

    def display_informations(self):
        super().display_informations()
        print(f"Edition: {self.edition}")

book1 = Book('Clean Code', 'Robert Cecil Martin', 'edition 1970' )

magazine1 = Magazine('A Sentinela', 'testemunhas de Jeová', '12 abril 2023')

book2 = Book('William Shakespeare.', 'Hamlet.', 'Intelligence.' )

maganize2 = Magazine('Veja', 'Veja', 'January 2024.')

print("Informations Books:")
book1.display_informations()
book2.display_informations()


print("Informations Magazines:")
magazine1.display_informations()
maganize2.display_informations()
        