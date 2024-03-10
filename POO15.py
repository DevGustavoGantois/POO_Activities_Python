#Crie uma classe Aluno em Python com atributos privados,
#como nome, idade e matrícula. Implemente métodos
#públicos para acessar e modificar esses atributos. Em
#seguida, crie uma instância da classe e demonstre como
#usar os métodos de acesso.

class Student:
    def __init__(self, name, age, register_number):
        self.__name = name
        self.__age = age
        self.__register_number = register_number

    def get_name_student(self):
        return self.__name
        
    def get_age_student(self):
        return self.__age
        
    def get_register_student(self):
        return self.__register_number
    
    def set_name_student(self, name):
        self.__name = name
    
    def set_age_student(self, age):
        self.__age = age
    def set_register_student(self, register_number):
        self.__register_number = register_number

#Mostrando o uso:
student1 = Student('Gustavo Gantois', 20, 431256)

#Acessando os atributos utilizando o método GETTERS.
print(f"Name:{student1.get_name_student()}")
print(f"Age:{student1.get_age_student()}")
print(f"Register Number:{student1.get_register_student()}")

#Modificando os atributos utilizando o método SETTERS.
student1.set_name_student('Augusto')
student1.set_age_student(58)
student1.set_register_student(5674892)

#Exibindo os atributos após a sua modificação:
print("\nAfter modifications:")
print(f"Name:{student1.get_name_student()}")
print(f"Age:{student1.get_age_student()}")
print(f"Register Number:{student1.get_register_student()}")
