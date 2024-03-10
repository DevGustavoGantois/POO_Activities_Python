#Desenvolva uma classe ContaBancaria em Python com atributos
#privados, como saldo e número da conta. Forneça métodos
#públicos para depositar dinheiro, sacar dinheiro e verificar o
#saldo. Garanta que o saldo não seja definido como negativo e
#que as transações sejam registradas.

#OBS: Utilizei mais comentários que o normal para uma fixação melhor da lógica do meu código.

class Bank_Account:
    #Incluindo os atributos propostos pela atividade:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number
    #Mostrando os atributos privados criando métodos para retorna-los:
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
    #Utilizando o set mostrando que caso o valor do saldo for negativo ele não dara error e senão imprimirá o atributo privado balance de forma normal.
    def set_balance(self, balance):
        if balance < 0:
            raise ValueError("This balance is negative")
        elif balance > 0:
            self.__balance = balance

#Dando o valor do saldo e o número da conta:
account1 = Bank_Account(45.88, 2)
#Mostrando os valores atribuindo os métodos get_balance e get_account_number a account 1:
print(f"Initial Balance: {account1.get_balance()}")
print(f"Account Number: {account1.get_account_number()}")

try:
    account1.set_balance(60.000)
    print(f"The Balance is altered to: {account1.get_balance()}")
except ValueError as e:
    print(e)

#Caso mostre um caso que o saldo é negativo:

try:
    account1.set_balance(-231.5)
    print(f"The Balance is altered to: {account1.get_balance()}")
except ValueError as e:
    print(e)

