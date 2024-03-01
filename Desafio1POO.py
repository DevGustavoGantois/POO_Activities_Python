#Crie um sistema de gerenciamento de contas bancárias em Python usando herança e polimorfismo. O sistema deve incluir as seguintes classes: Classe Conta:
#-A classe base "Conta " deve ter atributos para o número da conta, o titular da conta e o saldo. -Ela deve incluir métodos para depósitos, saques e exibição do saldo
#atual. Classe Conta: -A classe base "Conta " deve ter atributos para o número da conta, o titular da conta e o saldo.



#-Ela deve incluir métodos para depósitos, saques e exibição do saldo atual. Classe ContaCorrente: -A classe "ContaCorrente
#" herda de"Conta"e inclui atributos específicos, como taxa de manutenção e limite de cheque especial. -Deve sobrescrever o método de saque para
#considerar o limite de cheque especial, se necessário. 



#Classe ContaPoupanca:-A classe"ContaPoupanca" também herda de"Conta"
#e inclui atributos específicos, como taxa de juros. -Ela deve ter um método para calcular e adicionar juros ao saldo. Polimorfismo:
#-Crie um método chamado resumo que pode ser chamado em qualquer objeto de conta (ContaCorrente ou
#ContaPoupanca). Esse método resumo irá exibir um resumo das informações da conta, incluindo o tipo de conta
#(corrente ou poupança), o número da conta, o titular da conta e o saldo atual. Teste de Funcionalidade:
#Crie um programa principal que demonstre o uso dessas classes. Crie instâncias de contas correntes e poupanças, realize depósitos,
#saques, adicione juros e chame o método resumo para cada conta.

class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successfully made.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successfully made.")
        else:
            print("Insufficient balance.")

    def summary(self):
        print(f"\nAccount Summary:")
        print(f"Account Type: General Account")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance, maintenance_fee, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.maintenance_fee = maintenance_fee
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrawal of {amount} successfully made.")
        else:
            print("Insufficient balance or exceeded overdraft limit.")

    def summary(self):
        super().summary()
        print(f"Account Type: Checking Account")
        print(f"Maintenance Fee: {self.maintenance_fee}")
        print(f"Overdraft Limit: {self.overdraft_limit}")


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest calculated and added to the account: {interest}")

    def summary(self):
        super().summary()
        print(f"Account Type: Savings Account")
        print(f"Interest Rate: {self.interest_rate}")


def main():
    print("Welcome to the Banking Account Management System!\n")

    account_number = int(input("Enter the account number: "))
    account_holder = input("Enter the account holder's name: ")
    initial_balance = float(input("Enter the initial balance of the account: "))

    account = Account(account_number, account_holder, initial_balance)

    while True:
        print("\nChoose an operation:")
        print("1 - Deposit")
        print("2 - Withdraw")
        print("3 - Account Summary")
        print("4 - Exit")

        choice = input("Enter the number of the desired operation: ")

        if choice == '1':
            deposit_amount = float(input("Enter the deposit amount: "))
            account.deposit(deposit_amount)

        elif choice == '2':
            withdrawal_amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(withdrawal_amount)

        elif choice == '3':
            account.summary()

        elif choice == '4':
            print("System closed. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
