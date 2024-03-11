#sistema de biblioteca
#Imagine um sistema de biblioteca em Python que gerencia livros e usuários. As classes envolvidas são Livro, Usuario, Biblioteca e Emprestimo.

#A classe Livro deve ter atributos privados, como título e autor, e métodos públicos para obter esses atributos.

#A classe Usuario deve ter atributos privados, como nome e ID, e métodos públicos para obter e modificar esses atributos.

#A classe Biblioteca deve conter uma lista de livros disponíveis
#e métodos para adicionar e remover livros. A classe Empréstimo deve representar um empréstimo de um livro por um
#usuário e deve estar associada a um Livro e a um Usuário. O exercício é criar essas classes, estabelecer a associação
#entre elas (um usuário pode pegar emprestado um livro da biblioteca), 
#aplicar encapsulamento para proteger os atributos privados e implementar métodos para:

class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
    
    def get_title_book(self):
        return self.__title
    def get_author_book(self):
        return self.__author
    def set_title_book(self, title):
        self.__title = title
    def set_author_book(self, author):
        self.__author = author



class User:
    def __init__(self, name, user_id):
        self.__name = name
        self.__user_id = user_id

    def get_name_user(self):
        return self.__name
    def get_user_id(self):
        return self.__user_id
    
    def set_name_user(self, name):
        self.__name = name
    def set_user_id(self, user_id):
        self.__user_id = user_id

class Library:
    def __init__(self):
        self.list_library = []

    def add_book(self, book):
        self.list_library.append(book)
    def remove_book(self, book):
        self.list_library.remove(book)    
    def display_books(self):
        print("Books available in Library:")
        for book in self.list_library:
            print(f"{book.get_title_book()}")

class Loan:
    def __init__(self, book, user):
        self.__book = book
        self.__user = user
        self.__is_returned = False
    def get_book(self):
        return self.__book
    def get_user(self):
        return self.__user
    def is_returned(self):
        return self.__is_returned
    def return_book(self):
        self.__is_returned = True

book1 = Book('Diário de um Banana', 'Jeff Kinney')
user1 = User('Gustavo Gantois', '09745')
book2 = Book('A divina comédia','Dante Alighieri')
user2 = User('Jorge Augusto', '3578')

library = Library()
library.add_book(book1)
library.add_book(book2)

library.display_books()

loan1 = Loan(book1, user1)
loan2 = Loan(book2, user2)

print(f"\nThe Book 1 is: {book1.get_title_book()}/Author 1: {book1.get_author_book()}")
print(f"\nThe User 1 is: {user1.get_name_user()}/ID User 1: {user1.get_user_id()}")
print(f"\nThe Book 2 is: {book2.get_title_book()}/Author 2: {book2.get_author_book()}")
print(f"\nThe User 2 is: {user2.get_name_user()}/ID User 2: {user2.get_user_id()}")
print(f"\nLoan Details:\nUser: {loan1.get_user().get_name_user()}, Book: {loan1.get_book().get_title_book()}")
print(f"Is Returned: {loan1.is_returned()}")

loan1.return_book()
print(f"Is Returned: {loan1.is_returned()}")

#Podemos também utilizar um método para encapsular a string usando def __str__(self) retornando a frase com o titulo e o autor e assim por diante.