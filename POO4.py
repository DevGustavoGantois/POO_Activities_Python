#Crie uma classe Calculadora que tenha métodos
#para realizar operações matemáticas básicas (+ , - ,*, / ).

class Calculator:
    def __init__(self): 
        print("CALCULATOR")
        print("<==========================>")
        print("1- Adiction")
        print("2- Subtract")
        print("3- Multiply")
        print("4- Divide")
        print("<========================>")
        self.option = int(input("Enter your option:"))
        self.num1 = float(input("Enter a number 1:"))
        self.num2 = float(input("Enter a number 2:"))

    def add(self):
        result = self.num1 + self.num2
        return result
    def subtract(self):
        result = self.num1 - self.num2
        return result
    def multiply(self):
        result = self.num1 * self.num2
        return result    
    def divide(self):
        result = self.num1 / self.num2
        return result

calculator = Calculator()


if calculator.option == 1:
    print("Result:", calculator.add())
elif calculator.option == 2:
    print("Result:", calculator.subtract())
elif calculator.option == 3:
    print("Result:", calculator.multiply())
elif calculator.option == 4:
    print("Result:", calculator.divide())
else:
    print("Invalid option.")