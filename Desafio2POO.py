#A classe Biblioteca deve conter uma lista de
#livros disponíveis e métodos para adicionar e
#remover livros.

#-A classe Empréstimo deve representar um
#empréstimo de um livro por um usuário e deve estar associada a um Livro e a um Usuário.

#O exercício é criar essas classes, estabelecer a associação
#entre elas (um usuário pode pegar emprestado um livro da
#biblioteca), aplicar encapsulamento para proteger os
#atributos privados e implementar métodos para:

#-Adicionar e remover livros da biblioteca.

#-Registrar um empréstimo de livro por um usuário, verificando se o livro
#está disponível.

#-Exibir informações sobre os empréstimo, como qual livro foi emprestado
#para qual usuário.

class Book:
    def __init__(self, title):
        self.title = title 
        self.is_available = True        
class User:
    def __init__(self, username):
        self.username = username
class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def remove_books(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"The book: {book} is removed from the library.")
        else:
            print("The book is not exist.")

    def display_books(self):
            print("Books:")
            for book in self.books:
                print(book.title)

class Loan:
    def __init__(self, user, book, library):
        self.user = user
        self.book = book
        self.library = library
    
    def borrow_book(self):
        if self.book.is_available:
            self.book.is_available = False
            print(f"{self.user.username} borrowed {self.book.title}")
        else:
            print(f"Sorry, {self.book.title} is not available for borrowing.")
    def returned_book(self):
        if self.book.is_available:
            self.book.is_available = True
            print(f"{self.username} returned {self.book.title} from library.")
        else:
            print(f"{self.book.title} is already available in the library") 

library = Library()

book1 = Book('Clean Code')
book2 = Book('The secrets of python')
book3 = Book("O segredo da mente milionária")
library.add_books(book1) 
library.add_books(book2)
library.add_books(book3)

#Mostrando os livros da livraria.
library.display_books()

#Criando o usuário:
user1 = User('Gustavo')
user2 = User('Augusto')
user3 = User('Nayra')

#Usando os livros emprestados:
loan1 = Loan(user1, book1, library)
loan1.borrow_book()

#Mostrando os livros:
library.display_books()

#retornado os livros:
loan1.returned_book()

#Mostrando os livros depois que retornaram:
library.display_books()
                
