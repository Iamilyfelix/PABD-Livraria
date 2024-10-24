#aqui conecta o usuario ao bd
import psycopg2
from backend.usuario import Usuario#tava dando erro aq
class UsuarioBanco:
    #usamos essa função pra fazer o login
    # essa função vai na tabela usuario ve se tem o nome e senha la e se tiver autoriza o login 
    def pegar_usuario_por_username(self,username_func):
        db_connection = psycopg2.connect(dbname='livraria',
                                         user="postgres",
                                         password="pabd",
                                         host='localhost',
                                         port=5432)
        db_cursor=db_connection.cursor()#isso aq é um comando da biblioteca para se conectar com o bd
        comando_sql="SELECT * FROM usuarios WHERE username = '" + username_func + "';"
        print(comando_sql)
        db_cursor.execute(comando_sql)
        linhas_banco_dados=db_cursor.fetchone()#aqui fala que as linhas bd vai receber o fetoche que retorna uma tupla
        db_connection.commit()#Este comando confirma qualquer operação de alteração de dados no banco, como INSERT, UPDATE ou DELETE. No seu caso, como você está apenas fazendo um SELECT
        db_connection.close()#Encerra a conexão com o banco de dados. 
        if linhas_banco_dados != None:
            nome_usuario=linhas_banco_dados[0]
            username_usuario=linhas_banco_dados[1]
            senha_usuario=linhas_banco_dados[2]
            #Essas linhas de código são fundamentais para capturar os dados retornados da consulta SQL e armazená-los em variáveis para posterior uso, como a criação de um objeto que representa o usuário no seu sistema
            usuario = Usuario(nome_usuario,username_usuario,senha_usuario)

        else:
            usuario=None
        
        return usuario