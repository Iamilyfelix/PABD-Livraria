class Livros:

    def __init__(self, nome, autor, genero, cod):
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.cod = cod

    def __repr__(self):#retorna o nome do objeto ex:nome
        return self.nome

    def get_nome(self):#aq retorna o valor do obejeto ex:é assim que acaba 
        return self.nome
    

