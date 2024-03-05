#A classe principal será chamada de "Material" e terá um construtor que recebe dois parâmetros: FEITO
#"titulo" e "autor_ou_editora". Essa classe também terá um método chamado "exibir_informacoes"  FEITO
#que imprimirá na saída o título e o autor/editora do material.
#A classe "Livro" será uma subclasse da classe "Material" e terá um construtor que recebe três parâmetros: 
#"titulo", "autor_ou_editora" e "genero". Essa classe também terá um método "exibir_informacoes" que chamará o método correspondente 
#na classe "Material" e imprimirá o gênero do livro.
#A classe "Revista" será outra subclasse da classe "Material" e terá um construtor que recebe três parâmetros: 
#"titulo", "autor_ou_editora" e "edicao". Essa classe também terá um método "exibir_informacoes" que chamará o método correspondente na 
#classe "Material" e imprimirá a edição da revista.
#Crie instâncias das classes "Livro" e "Revista" com informações específicas e chame o método "exibir_informacoes" 
#para mostrar os detalhes de cada material

class Material:
    def __init__(self, title, author_or_publisher):
        self.title = title
        self.author_or_publisher = author_or_publisher

    def display_information(self):
        print(f''' Material Title: {self.title}
Author or Publisher: {self.author_or_publisher}
''')

class Book(Material):
    def __init__(self, title, author_or_publisher, genre):
        super().__init__(title, author_or_publisher)
        self.genre = genre
    
    def display_information(self):
        super().display_information()
        print(f'Book Genre: {self.genre}')

class Magazine(Material):
    def __init__(self, title, author_or_publisher, edition):
        super().__init__(title, author_or_publisher)
        self.edition = edition

    def display_information(self):
        super().display_information()
        print(f'Edition: {self.edition}')

book1 = Book('The Art of War.', 'Sun Tzu.', 'Emotional Intelligence.')
magazine1 = Magazine('National Geographic.', 'National Geographic Society.', 'April 2022.')
book2 = Book('William Shakespeare.', 'Hamlet.', 'Intelligence.' )
magazine2 = Magazine('Veja', 'Veja', 'January 2024.')
book3 = Book('The Three Musketeers.', 'Alexandre Dumas.', 'Classic.')
magazine3 = Magazine('Viva Mais', 'Viva Mais', 'March 2020.')

print("Book Information:")
book1.display_information()
book2.display_information()
book3.display_information()

print("\nMagazine Information:")
magazine1.display_information()
magazine2.display_information()
magazine3.display_information()
