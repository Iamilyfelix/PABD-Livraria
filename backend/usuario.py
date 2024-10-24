#class criada pra usuario, usada em 
class Usuario:
    def __init__(self):
        self.nome
        self.username  = None #aqui estou defininfo none pq inicializa sem valor
        self.senha  = None
    
    def __init__(self, nome_func,username_func, senha_func):#aqui estou dando os parametros pra quando eu for usar essa classe eu passar esses nomes por parametro
        self.nome=nome_func
        self.username  = username_func
        self.senha  = senha_func

    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome
    
    def get_senha(self):
        return self.senha