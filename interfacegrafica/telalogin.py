import tkinter as tk
from backend.usuarioconect import UsuarioBanco
from interfacegrafica import telahome

mywindow = None
textb = None
textb_senha = None #coloca isso no começo pra dizer que o progama começa com nada 

def buttonpress():
    global textb
    global textb_senha
    global mywindow
    global label#dizendo que são variaveis globais e que podem ser usadas fora da função

    print("Pessoa digitou o username: "  + textb.get())#está imprimindo os valores digitados no terminal para ver o que foi inserido nos campos de usuário e senha.
    print("Pessoa digitou a senha   : "  + textb_senha.get())
    username_digitado    = textb.get()#guarda o usuario
    senha_digitado   = textb_senha.get()#textb senha guarda a senha  

    gerenciador_usuario = UsuarioBanco()#dizendo que o objeto recebe a classe 
    usuario_banco = gerenciador_usuario.pegar_usuario_por_username(username_digitado)
    #aqui a gente ta testando se o nome digitado ta no bd 
    if usuario_banco !=None:#se o retorno da função acima for diferente de nada, entre 
        if senha_digitado==usuario_banco.get_senha():#se a senha digitada for igual a senha do banco imprima login sucesso 
            label.config(text="Você fez login com sucesso!!!")
            print("O usuario fez login com sucesso")
            telahome.run()#aqui se o login for sucedido aparece a tela home que é a segunda tela 
        else:
            label.config(text="Senha incorreta!")
            print("o usuario digitou a senha errada")
        
    else:
        label.config(text="Usuario não encontrado!!!")
        print("usuario não encontrado")

def textBox():
    print(textb.get())

def run():# essa é a função que roda a tela
    global textb
    global textb_senha
    global mywindow
    global label

    mywindow = tk.Tk()
    mywindow.title("Tela de Login") # Título da janela
    mywindow.geometry("500x300")  # Definindo tamanho da janela

    # Label para o título
    label = tk.Label(mywindow, text="faça login",font=("Arial", 16, "bold"), fg="blue")#titulo
    label.grid(row=0,column=1)

    button = tk.Button(mywindow,text='Login',command=buttonpress,font=("Arial", 12), bg="green", fg="white")#quando o usuario clica no botão o comando button press é ativado, definimos a função la em cima que é a função que guarda a senha digitada e ver se tem o username e senha no bd se tiver faz o login se não tiver barra o login
    button.grid(row=3,column=1)

    #Textusername
    textb_label = tk.Label(mywindow, text="Username:")
    textb_label.grid(row=1, column=0, sticky="e")
    textb = tk.Entry(mywindow,text="Entry")
    textb.grid(row=1,column=1)

    textb_senha_label = tk.Label(mywindow, text="Senha:")
    textb_senha_label.grid(row=2, column=0, sticky="e")
    textb_senha = tk.Entry(mywindow,show="*")
    textb_senha.grid(row=2,column=1)

    mywindow.mainloop()