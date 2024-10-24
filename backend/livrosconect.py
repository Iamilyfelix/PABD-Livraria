import psycopg2
from backend.livros import Livros
class LivrosBanco:
    #essa função retorna uma lista de livros 
    #usamos ela na listbox
    def pegar_todos_livros(self,atributo):
        db_connection = psycopg2.connect(dbname='livraria',
                                         user="postgres",
                                         password="pabd",
                                         host='localhost',
                                         port=5432)
        db_cursor = db_connection.cursor()

        comando_sql="SELECT " + atributo + " FROM livro;"
        print(comando_sql)
        
        db_cursor.execute(comando_sql)

        lista_livros  = db_cursor.fetchall()# Retorna todas as linhas que foram encontradas pela consulta SQL. O resultado será uma lista de tuplas, onde cada tupla representa um registro (ou linha) da tabela
        
        db_connection.commit()#confirma a transação quando executar alterações na tabela pois elas ficam em estado de transação 
        db_connection.close()#fecha a conexão com o bd

        lista_livros_final=[]#cria uma lista vazia 
        
        for livro_banco in lista_livros:#para cada livro em lista livro
            nome=livro_banco[0] #nome recebe livro do banco na posição 0
            autor=livro_banco[1]
            genero=livro_banco[2]
            cod=livro_banco[3]

            livro_item=Livros(nome,autor,genero,cod)# livro intem recebe a classe livros
            lista_livros_final.append(livro_item)#adicionte os itens do livro intem a lista de livros final 
        return lista_livros_final#retorne a lista de livros 
        
    def inserir_livros(self,nome,autor,genero,cod):
        db_connection = psycopg2.connect(dbname='livraria',
                                         user="postgres",
                                         password="pabd",
                                         host='localhost',
                                         port=5432)
        db_cursor = db_connection.cursor()
        comando_sql="INSERT INTO livro VALUES ('" + nome + "', '" + autor + "', '" + genero + "', " + cod + ");"
        print(comando_sql)
        cursor = db_connection.cursor()
        db_cursor.execute(comando_sql)
        db_connection.commit()
        db_connection.close()

    def remover_livros(self,nome):
        db_connection = psycopg2.connect(dbname='livraria',
                                         user="postgres",
                                         password="pabd",
                                         host='localhost',
                                         port=5432)
        db_cursor = db_connection.cursor()
        comando_sql = "DELETE FROM livro WHERE nome = %s;"
        db_cursor.execute(comando_sql, (nome,))
        print(comando_sql)

        if db_cursor.rowcount == 0:
            print(f"Livro '{nome}' não encontrado.")  # Mensagem de erro
        else:
            print(f"Livro '{nome}' removido com sucesso.")  # Mensagem de sucesso

        db_connection.commit()
        db_cursor.close()
        db_connection.close()

    def editar_livros(self, nome, novo_nome, novo_autor, novo_genero, novo_cod):
        db_connection = psycopg2.connect(dbname='livraria',
                                     user="postgres",
                                     password="pabd",
                                     host='localhost',
                                     port=5432)
        db_cursor = db_connection.cursor()#uma função do psycopg2 que permite a execução do comando sql
    
        # Comando SQL para atualizar o livro
        comando_sql = """
        UPDATE livro
        SET nome = %s, autor = %s, genero = %s, cod = %s
        WHERE nome = %s;
        """
        db_cursor.execute(comando_sql, (novo_nome, novo_autor, novo_genero, novo_cod, nome))
        
        # para verificar se a consulta retornou algum resultado pra gente ter controle da situação
        if db_cursor.rowcount == 0:
            print(f"Livro '{nome}' não encontrado para edição.")  # Mensagem de erro
        else:
            print(f"Livro '{nome}' atualizado com sucesso.")  # Mensagem de sucesso

        db_connection.commit()
        db_cursor.close()
        db_connection.close()
    
        
    