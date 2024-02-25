#Crie uma classe Empresa que permita gerenciar
#funcionários. Os funcionários devem ter informações
#como nome, cargo e salário. A empresa deve ser capaz
#de adicionar, remover e listar funcionários.

class Company:
    def __init__(self):
        self.informations_company =[]   

    def add_employees(self):
        name = input("Enter your name:")
        office = input("Enter your office:")
        salary = float(input("Enter your salary:"))
        add_informations = {'name': name, 'office': office, 'salary': salary}
        self.informations_company.append(add_informations)    

    def list_employees(self):
        print("Listing Again:")
        for employee in self.informations_company:
            print(employee)

    def remove_employees(self):
        name_to_remove = input("Which employee do you want to remove?")
        for employee in self.informations_company:
            if employee['name'] == name_to_remove:
                self.informations_company.remove(employee)
                print(f"Removed employee: {name_to_remove} is sucessfully.")

    def main(self):
        while True:
            print("LIST OF EMPLOYEES IN COMPANY")
            print("<=============================>")
            print("1- Adding employee.")
            print("2- List the functions again.")
            print("3- Removing employee.")
            print("4-Exit the program.")
            print("<=============================>")

            option = int(input("Enter a option:"))

            if option == 1:
                result = self.add_employees()
                return result
            elif option == 2:
                result = self.list_employees()
            elif option == 3:
                result = self.remove_employees()
            elif option == 4:
                print(f"Finished the program...")
                break

if __name__ == '__main__':
    company_instance = Company()
    company_instance.main()
