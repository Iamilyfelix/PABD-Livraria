import psycopg2
from backend.emprestimo import Emprestimo

class EmprestimoBanco:

    def pegar_todos_emprestimos(self,atributo):
        db_connection = psycopg2.connect(dbname='livraria',
                                         user="postgres",
                                         password="pabd",
                                         host='localhost',
                                         port=5432)
        db_cursor = db_connection.cursor()

        comando_sql="SELECT " + atributo + " FROM emprestimo;"
        print(comando_sql)
        db_cursor.execute(comando_sql)#manda executar
        lista_emprestimo  = db_cursor.fetchall()
        print(lista_emprestimo)

        db_connection.commit()
        db_connection.close()

        lista_emprestimo_final=[]

        for emprestimo_banco in lista_emprestimo:
            nome_livro=emprestimo_banco[0]
            nome_cliente=emprestimo_banco[1]
            data_inicial=emprestimo_banco[2]
            data_final=emprestimo_banco[3]

            emprestimo=Emprestimo(nome_livro,nome_cliente,data_inicial,data_final)#aq pega a tupla e retorna objeto
            lista_emprestimo_final.append(emprestimo)#aqui pega o objeto e joga pra lista
        return lista_emprestimo_final
    
    def inserir_emprestimo(self,nome_livro,nome_cliente,data_inicial,data_final):
        db_connection = psycopg2.connect(dbname='livraria',
                                         user="postgres",
                                         password="pabd",
                                         host='localhost',
                                         port=5432)
        db_cursor = db_connection.cursor()
        comando_sql="INSERT INTO emprestimo VALUES ('" + nome_livro + "', '" + nome_cliente+ "', '" + data_inicial + "', '" + data_final + "');"

        db_cursor.execute(comando_sql, (nome_livro, nome_cliente, data_inicial, data_final))
        # db_cursor.execute(comando_sql)
        db_connection.commit()
        db_connection.close()


        # Verificar quantas linhas foram afetadas
        if db_cursor.rowcount == 0:
            print("não foi realizado a inserção.")  # Mensagem de erro
        else:
            print("deu certo a inserção")  # Mensagem de sucesso

 