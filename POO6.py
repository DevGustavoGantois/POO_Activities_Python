class Hotel:
    def __init__(self):
        self.employees = []
        self.reservations = []

    def add_employee(self, name, function, salary):
        employee_information = {'name': name, 'function': function, 'salary': salary}
        self.employees.append(employee_information)

    def receive_reservation(self, reserve, bedroom, nights):
        reservation_information = {'reserve': reserve, 'bedroom': bedroom, 'nights': nights}
        self.reservations.append(reservation_information)

    def calculate_bill(self):
        total_salary = sum(employee['salary'] for employee in self.employees)
        total_nights = sum(reservation['nights'] for reservation in self.reservations)
        bill = total_salary + total_nights * 100  # Assuming a nightly rate of $100
        return bill

# Criando uma instância da classe Hotel
hotel = Hotel()

# Adicionando funcionários
name = input("Enter a name of employee:")
function = input("Enter a function of employee:")
salary = float(input("Enter a salary of employee:"))
hotel.add_employee(name, function, salary)

# Recebendo uma reserva
reserve = input("Enter a reserve:")
bedroom = int(input("Enter your bedroom:"))
nights = int(input("How many nights will you stay:"))
hotel.receive_reservation(reserve, bedroom, nights)

# Calculando a conta final
total_bill = hotel.calculate_bill()

print(f"Total Bill: ${total_bill}")


