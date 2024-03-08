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