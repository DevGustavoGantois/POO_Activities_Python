#Crie uma classe chamada"Calculadora"com um método"
#somar"que pode somar dois números inteiros ou duas
#strings. Use o polimorfismo para implementar a sobrecarga do método"
#somar"para que ele funcione
#com diferentes tipos de entrada (números inteiros e
#strings). Crie exemplos de uso para demonstrar como a
#mesma função pode se comportar de maneira diferente com base nos tipos de entrada.

#1) FORMA DE RESOLVER, UTILIZANDO O POLIMORFISMO E INSTANCIANDO AS VARIÁVEIS ATRIBUINDO ELAS A INT E STRING.
class Calculator: #Decorador indicando o método.
    @staticmethod
    def sum_letters_and_numbers(num1, num2, string1, string2):
        if isinstance(num1, int) and isinstance(num2, int): #isinstance usado para verificar se num1, num2 são int e se string1 e string2 são str.
            return num1 + num2
        elif isinstance(string1, str) and isinstance(string2, str):
            return string1 + string2
        else:
            raise ValueError("Invalid input types...")

if __name__ == "__main__":
    while True:
            print("CALCULATOR STRING AND NUMBERS")
            print("<==============================>")
            print("1 - Sum numbers.")
            print("2 - Sum Strings.")
            print("3 - Exit the program.")
            print("<===============================>")
            
            option = int(input("Enter a option:"))

            if option == 1:
                number1 = int(input("Enter a number 1:"))
                number2 = int(input("Enter a number 2:"))
                result_sum_numbers = Calculator.sum_letters_and_numbers(num1=number1, num2=number2, string1=None, string2=None)
                print("Sum numbers: ",result_sum_numbers)
            elif option == 2:
                string1 = str(input("Enter a phrase 1:"))
                string2 = str(input("Enter a phrase 2:"))
                result_sum_strings = Calculator.sum_letters_and_numbers(num1=None, num2=None, string1=string1, string2=string2)
                print("Sum strings: ",result_sum_strings)
            elif option == 3:
                print("Exit the program.")
                break
            else:
                print("Invalid option. Please enter a valid option.")

#2)FORMA DE RESOLVER UTILIZANDO O SUPER E PEGANDO OS SELF DA CLASSE PAI.
#class Calculator:
    #def __init__(self, num1, num2, string1, string2):
        #self.num1 = num1
        #self.num2 = num2
        #self.string1 = string1
        #self.string2 = string2

    #def sum_letters_and_numbers(self):
        #if self.num1 == type(int) and self.num2 == type(int):
            #super().sum_letters_and_numbers( self.num1 + self.num2)
        #elif self.string1 == type(str) and self.string2 == type(str):
            #super().sum_letters_and_numbers(self.string1 + self.string2)

#if __name__ == "__main__":
    #while True:
            #print("CALCULATOR STRING AND NUMBERS")
            #print("<==============================>")
            #print("1 - Sum numbers.")
            #print("2 - Sum Strings.")
            #print("3 - Exit the program.")
            #print("<===============================>")
            
            #option = int(input("Enter a option:"))

            #if option == 1:
                #number1 = int(input("Enter a number 1:"))
                #number2 = int(input("Enter a number 2:"))
                #result_sum_numbers = (number1 + number2)
                #print("Sum numbers: ",result_sum_numbers)
            #elif option == 2:
                #string1 = str(input("Enter a phrase 1:"))
                #string2 = str(input("Enter a phrase 2:"))
                #result_sum_strings = (string1 + string2)
                #print("Sum strings: ",result_sum_strings)
            #elif option == 3:
                #print("Exit the program.")
                #break
            #else:
                #print("Invalid option. Please enter a valid option.")