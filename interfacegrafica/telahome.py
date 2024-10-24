import tkinter as tk
from backend.livrosconect import LivrosBanco
from interfacegrafica.telaemprestimo import *

mywindow2 = None
textb = None
textb_senha = None
textbnome_inserir = None
textbautor_inserir = None
textbgenero_inserir = None
textbcod_inserir = None
textbnome_remover=None
def buttonPressInserir():
    global textbnome_inserir, textbautor_inserir, textbgenero_inserir, textbcod_inserir
    # Pegar os dados da entrada de texto
    nome = textbnome_inserir.get()
    autor = textbautor_inserir.get()
    genero = textbgenero_inserir.get()
    cod = textbcod_inserir.get()

    # Inserir no banco de dados
    l = LivrosBanco()
    l.inserir_livros(nome, autor, genero, cod)
    messagebox.showinfo("Sucesso", f"Livro cadastrado com sucesso!\nLivro: {nome}\nAutor: {autor}\nGenero: {genero}\ncod: {cod}")
    # Atualizar a lista de livros
    preencher_lista_nome_livros()
    textbnome_inserir.delete(0, tk.END)
    textbautor_inserir.delete(0, tk.END)
    textbgenero_inserir.delete(0, tk.END)
    textbcod_inserir.delete(0, tk.END)

def buttonPressRemover():
    global textbnome_remover
    # Pegar o nome do livro a ser removido
    nome = textbnome_remover.get()

    # Remover no banco de dados
    r = LivrosBanco()
    r.remover_livros(nome)

    # Atualizar a lista de livros
    preencher_lista_nome_livros() 
    textbnome_remover.delete(0, tk.END)

def buttonPressEditar():
    global textbnome_editar, textbnovo_nome, textbnovo_autor, textbnovo_genero, textbnovo_cod
    nome = textbnome_editar.get()
    novo_nome = textbnovo_nome.get()
    novo_autor = textbnovo_autor.get()
    novo_genero = textbnovo_genero.get()
    novo_cod = textbnovo_cod.get()

    # Chamar a função de edição
    e= LivrosBanco()
    e.editar_livros(nome, novo_nome, novo_autor, novo_genero, novo_cod)

    preencher_lista_nome_livros()
    # Limpar os campos de entrada após a operação
    textbnome_editar.delete(0, tk.END)
    textbnovo_nome.delete(0, tk.END)
    textbnovo_autor.delete(0, tk.END)
    textbnovo_genero.delete(0, tk.END)
    textbnovo_cod.delete(0, tk.END)

def preencher_lista_nome_livros():
    global listbox 
    listbox.delete(0, tk.END)
    l = LivrosBanco()
    lista_livros_banco_dados  = l.pegar_todos_livros("*")#Chama o método pegar_todos_livros da classe LivrosBanco (usando o objeto l). O argumento "*" provavelmente significa que quer buscar todos os livros do banco. O resultado é armazenado na variável lista_livros_banco_dados, que deve ser uma lista de objetos de livros.

    print(f"Livros no banco: {lista_livros_banco_dados}")

    listbox.delete(0, tk.END)

    lista_nomes_livros = []
    for livro in lista_livros_banco_dados:
        lista_nomes_livros.append(livro.get_nome())
    
    lista_nomes_livros.sort(reverse=True)   
    for nome in lista_nomes_livros:
        listbox.insert(0, nome)

def run():
    global textbnome_inserir, textbautor_inserir, textbgenero_inserir, textbcod_inserir
    global textbnome_remover,listbox
    global textbnome_editar, textbnovo_nome, textbnovo_autor, textbnovo_genero, textbnovo_cod

    mywindow2 = tk.Tk()
    mywindow2.title("Inserir, Remover e Editar Livros")

    frame_listbox = tk.Frame(mywindow2)
    frame_listbox.grid(pady=10)

    tk.Label(frame_listbox, text="Lista de Livros:").grid(column=0,row=1)
    listbox = tk.Listbox(frame_listbox, width=50, height=10)
    listbox.grid()

    tk.Button(mywindow2, text="Tela emprestimo", command=abrir_tela_emprestimo).grid(row=0, column=3)

    # Frames para Inserir, Remover e Editar Livro
    frame_container = tk.Frame(mywindow2)
    frame_container.grid(pady=10)

    # Frame para Inserir Livro
    frame_inserir = tk.Frame(frame_container)
    frame_inserir.grid(row=0, column=0, padx=10)

    tk.Label(frame_inserir, text="Nome do Livro:").grid(row=0, column=0)
    textbnome_inserir = tk.Entry(frame_inserir)
    textbnome_inserir.grid(row=0, column=1)

    tk.Label(frame_inserir, text="Autor:").grid(row=1, column=0)
    textbautor_inserir = tk.Entry(frame_inserir)
    textbautor_inserir.grid(row=1, column=1)

    tk.Label(frame_inserir, text="Gênero:").grid(row=2, column=0)
    textbgenero_inserir = tk.Entry(frame_inserir)
    textbgenero_inserir.grid(row=2, column=1)

    tk.Label(frame_inserir, text="Código:").grid(row=3, column=0)
    textbcod_inserir = tk.Entry(frame_inserir)
    textbcod_inserir.grid(row=3, column=1)

    tk.Button(frame_inserir, text="Inserir Livro", command=buttonPressInserir).grid(row=4, columnspan=2, pady=10)

    # Frame para Remover Livro
    frame_remover = tk.Frame(frame_container)
    frame_remover.grid(row=0, column=1, padx=10)

    tk.Label(frame_remover, text="Nome do Livro a Remover:").grid(row=0, column=0)
    textbnome_remover = tk.Entry(frame_remover)
    textbnome_remover.grid(row=0, column=1)

    tk.Button(frame_remover, text="Remover Livro", command=buttonPressRemover).grid(row=1, columnspan=2, pady=10)

    # Frame para Editar Livro
    frame_editar = tk.Frame(frame_container)
    frame_editar.grid(row=0, column=2, padx=10)

    tk.Label(frame_editar, text="Nome do Livro a Editar:").grid(row=0, column=0)
    textbnome_editar = tk.Entry(frame_editar)
    textbnome_editar.grid(row=0, column=1)

    tk.Label(frame_editar, text="Novo Nome:").grid(row=1, column=0)
    textbnovo_nome = tk.Entry(frame_editar)
    textbnovo_nome.grid(row=1, column=1)

    tk.Label(frame_editar, text="Novo Autor:").grid(row=2, column=0)
    textbnovo_autor = tk.Entry(frame_editar)
    textbnovo_autor.grid(row=2, column=1)

    tk.Label(frame_editar, text="Novo Gênero:").grid(row=3, column=0)
    textbnovo_genero = tk.Entry(frame_editar)
    textbnovo_genero.grid(row=3, column=1)

    tk.Label(frame_editar, text="Novo Código:").grid(row=4, column=0)
    textbnovo_cod = tk.Entry(frame_editar)
    textbnovo_cod.grid(row=4, column=1)

    tk.Button(frame_editar, text="Editar Livro", command=buttonPressEditar).grid(row=5, columnspan=2, pady=10)


    # Preencher a listbox ao iniciar
    preencher_lista_nome_livros()
    
    # Iniciar a interface
    mywindow2.mainloop()
    
