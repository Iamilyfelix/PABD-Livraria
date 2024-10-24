import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.emprestimoconect import EmprestimoBanco


def realizar_emprestimo():#botão
    global nome_livro, nome_cliente, data_inicial, data_final

    nome_livro = nome_livro_realizar.get()
    nome_cliente = nome_cliente_realizar.get()
    data_inicial = data_inicial_realizar.get()
    data_final = data_final_realizar.get()
    
    r = EmprestimoBanco()
    r.inserir_emprestimo(nome_livro,nome_cliente,data_inicial,data_final)
    # Aqui você pode adicionar a lógica para registrar o empréstimo no banco de dados
    messagebox.showinfo("Sucesso", f"Empréstimo registrado com sucesso!\nLivro: {nome_livro}\nCliente: {nome_cliente}\nData Inicial: {data_inicial}\nData Final: {data_final}")
    prencher_lista_emprestimo()


def prencher_lista_emprestimo():#função que chamamos quando apertamos o botão realizar emprestimo
    global treeview 
    r=EmprestimoBanco()
    lista_emprestimo_banco=r.pegar_todos_emprestimos("*")

    print(f"emprestimos do banco{lista_emprestimo_banco}")
    
    for item in treeview.get_children():
        treeview.delete(item)

    # Verifica se há empréstimos recuperados
    if lista_emprestimo_banco:
        for emprestimo in lista_emprestimo_banco:#essa lista emprestimo a gente cirou la na emprestimo conect
            # Insere os dados de cada empréstimo em uma linha na Treeview
            treeview.insert("", "end", values=(emprestimo.nome_livro, emprestimo.nome_cliente, emprestimo.data_inicial, emprestimo.data_final))
    else:
        print("Nenhum empréstimo encontrado no banco de dados.")

def abrir_tela_emprestimo():#função que fica no botão da tela home
    global treeview
    global listbox
    global mywindow3
    global nome_livro_realizar, nome_cliente_realizar, data_inicial_realizar, data_final_realizar
    global nome_cliente_remover

    mywindow3 = tk.Tk()
    mywindow3.title("Realizar Emprestimo")

    frame_emprestimo = tk.Frame(mywindow3)
    frame_emprestimo.grid(pady=20)

    #lista de emprestimo
    frame_listbox= tk.Frame(mywindow3)
    frame_listbox.grid(pady=10)

    # Criação do Treeview
    treeview = ttk.Treeview(frame_listbox, columns=("Livro", "Cliente", "Data Inicial", "Data Final"), show="headings")

    # Definir cabeçalhos
    treeview.heading("Livro", text="Nome do Livro")
    treeview.heading("Cliente", text="Nome do Cliente")
    treeview.heading("Data Inicial", text="Data Inicial")
    treeview.heading("Data Final", text="Data Final")


    # Definir largura das colunas 
    treeview.column("Livro", width=150)
    treeview.column("Cliente", width=150)
    treeview.column("Data Inicial", width=100)
    treeview.column("Data Final", width=100)

    treeview.grid(row=0, column=0)


    # Labels e entradas para os dados do empréstimo
    tk.Label(frame_emprestimo, text="Nome do Livro:").grid(row=0, column=0, padx=10, pady=5)
    nome_livro_realizar = tk.Entry(frame_emprestimo)
    nome_livro_realizar.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_emprestimo, text="Nome do Cliente:").grid(row=1, column=0, padx=10, pady=5)
    nome_cliente_realizar = tk.Entry(frame_emprestimo)
    nome_cliente_realizar.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_emprestimo, text="Data Inicial:").grid(row=2, column=0, padx=10, pady=5)
    data_inicial_realizar = tk.Entry(frame_emprestimo)
    data_inicial_realizar.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_emprestimo, text="Data Final:").grid(row=3, column=0, padx=10, pady=5)
    data_final_realizar = tk.Entry(frame_emprestimo)
    data_final_realizar.grid(row=3, column=1, padx=10, pady=5)

    btn_realizar_emprestimo = tk.Button(frame_emprestimo, text="Realizar Empréstimo", command=realizar_emprestimo)
    btn_realizar_emprestimo.grid(row=4, columnspan=2, pady=20)

    # Labels e entradas para os dados do empréstimo
    tk.Label(frame_emprestimo, text="Nome do Livro:").grid(row=0, column=0, padx=10, pady=5)
    nome_livro_realizar = tk.Entry(frame_emprestimo)
    nome_livro_realizar.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_emprestimo, text="Nome do Cliente:").grid(row=1, column=0, padx=10, pady=5)
    nome_cliente_realizar = tk.Entry(frame_emprestimo)
    nome_cliente_realizar.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_emprestimo, text="Data Inicial:").grid(row=2, column=0, padx=10, pady=5)
    data_inicial_realizar = tk.Entry(frame_emprestimo)
    data_inicial_realizar.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_emprestimo, text="Data Final:").grid(row=3, column=0, padx=10, pady=5)
    data_final_realizar = tk.Entry(frame_emprestimo)
    data_final_realizar.grid(row=3, column=1, padx=10, pady=5)

    # Botão para realizar o empréstimo
    btn_realizar_emprestimo = tk.Button(frame_emprestimo, text="Realizar Empréstimo", command=realizar_emprestimo)
    btn_realizar_emprestimo.grid(row=4, columnspan=2, pady=20)

    prencher_lista_emprestimo()
    # Iniciar o loop da interface
    mywindow3.mainloop()
