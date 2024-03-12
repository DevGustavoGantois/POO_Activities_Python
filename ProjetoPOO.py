class Livro:
    def __init__(self, titulo, autor, id, status_emprestimo):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.status_emprestimo = status_emprestimo
class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_livros_emprestados = []
class Biblioteca:
    def __init__(self):
        self.lista_livros = []
        self.lista_membros = []
    
    def adiciona_livros(self, livros):
        self.lista_livros.append(livros)

    def adiciona_membros(self, membro):
        self.lista_membros.append(membro)

    def listar_membros_biblioteca(self):
        print('\nLista membros da biblioteca')
        for membro in self.lista_membros:
            print(membro.nome)
    
    def listar_livros_biblioteca(self):
        print("\nLista de livros da biblioteca:")
        for livro in self.lista_livros:
            print(livro.titulo)
          
    def emprestimo_livros(self,livro, membro):
        if livro in self.lista_livros and livro.status_emprestimo == "Disponivel":
            livro.status_emprestimo = "Emprestado"
            membro.historico_livros_emprestados.append(livro)
            return f'O membro {membro.nome} fez um emprestimo do livro: {livro.titulo}.'
        else:
            return f'O membro {membro.nome} não fez o emprestimo de nenhum livro.'

    def devolucao_livros(self, livro, membro):
        if livro in membro.historico_livros_emprestados:
            livro.status_emprestimo = 'Disponível.'
            membro.historico_livros_emprestados.remove(livro)
            return f'O membro: {membro.nome} pediu devolução do livro: {livro.titulo}.'
        else:
            return f'O membro: {membro.nome} não pediu devolução do livro: {livro.titulo}.'
        
    def pesquisar_livros_titulo_id(self, titulo=None, id=None):
        print("Pesquisando livros por titulo e por ID:")
        for livro in self.lista_livros:
            if (titulo is None or livro.titulo == titulo) and (id is None or livro.id == id):
                print(f"Título por nome: {livro.titulo}, ID: {livro.id}")
            





livro1 = Livro('A Liberdade é uma Luta Constante', 'Angela Davis', 1234, 'Emprestado')
livro2 = Livro('Amor na Vitrine', 'Regina Navarro Lins', 3124, 'Indisponível' )
livro3 = Livro('Tempo de cura: como podemos nos tornar seres humanso completos firmes e fortes', 'Monja Coen', 6785, 'Disponível')
livro4 = Livro('Felicência: entre a distopia e a utopia da felicidade no trabalho', 'Carla Furtado', 9854, 'Indisponível')

membro1 = Membro('Gustavo Gantois',1)
membro2 = Membro('Jorge Adolfo',2)
membro3 = Membro('Matheus de Andrade',3)
membro4 = Membro('Yuri Santos',4)

biblioteca = Biblioteca()

# Adicionando livros à biblioteca
biblioteca.adiciona_livros(livro1)
biblioteca.adiciona_livros(livro2)
biblioteca.adiciona_livros(livro3)
biblioteca.adiciona_livros(livro4)
# Adicionando membros à biblioteca
biblioteca.adiciona_membros(membro1)
biblioteca.adiciona_membros(membro2)
biblioteca.adiciona_membros(membro3)
biblioteca.adiciona_membros(membro4)

#Listando livros da biblioteca:
biblioteca.listar_livros_biblioteca()
# Listando membros da biblioteca:
biblioteca.listar_membros_biblioteca()

#Caso queria fazer emprestimo dos livros, devolução...só instanciar as classes.
