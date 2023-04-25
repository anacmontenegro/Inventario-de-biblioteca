# ------- IMPORTAR TKINTER -------
from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# ------- IMPORTAR PILLOW -------
from PIL import Image, ImageTk

# ------- IMPORTAR CALENDÁRIO -------
from tkcalendar import Calendar, DateEntry
from datetime import date

# ------- IMPORTAR VIEW -------
from view import *

# ------- CORES -------
co0 = "#2e2d2b" # Preto
co1 = "#feffff" # Branco
co2 = "#403d3d" # Letra
co3 = "#00764C" # Verde
co4 = "#0056DD" # Azul 
co5 = "#A43E00" # Laranja 
co6 = "#D1D6D7" # Cinza p/ botões

# ------- CRIAR JANELA -------
janela = Tk()
janela.title = ('')
janela.geometry('900x642')
janela.configure(background=co6)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# ------- CRIAR FRAMES -------
frameCima = Frame(janela, width=900, height=55, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=900, height=341, bg=co1)
frameMeio.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=900, height=210, bg=co1)
frameBaixo.grid(row=2, column=0, pady=1, padx=0, sticky=NSEW)

# ------- CRIAR FUNÇÕES -------
global tree

# ------- FUNÇÃO INSERIR LIVRO -------
def inserir():
    global imagem, imagem_str, label_imagem
    nome = e_nome.get()
    autor = e_autor.get()
    isbn = e_isbn.get()
    editora = e_editora.get()
    data_da_compra = e_data_compra.get()
    valor_da_compra = e_valor.get()
    obs = e_descricao.get()
    imagem = imagem_str

    lista_inserir = [nome, autor, isbn, editora, data_da_compra, valor_da_compra, obs, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos.')
            return

    inserir_livro(lista_inserir)
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso.')

    e_nome.delete(0, 'end')
    e_autor.delete(0, 'end')
    e_isbn.delete(0, 'end')
    e_editora.delete(0, 'end')
    e_data_compra.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_descricao.delete(0, 'end')
    
    mostrar()

# ------- FUNÇÃO ATUALIZAR -------
def atualizar():
    global imagem, imagem_str, label_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0, 'end')
        e_autor.delete(0, 'end')
        e_isbn.delete(0, 'end')
        e_editora.delete(0, 'end')
        e_data_compra.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_descricao.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_autor.insert(0, treev_lista[2])
        e_isbn.insert(0, treev_lista[3])
        e_editora.insert(0, treev_lista[4])
        e_data_compra.insert(0, treev_lista[5])
        e_valor.insert(0, treev_lista[6])
        e_descricao.insert(0, treev_lista[7])
        imagem_str = treev_lista[8]

        ver_imag()

        def update():
            nome = e_nome.get()
            autor = e_autor.get()
            isbn = e_isbn.get()
            editora = e_editora.get()
            data_da_compra = e_data_compra.get()
            valor_da_compra = e_valor.get()
            obs = e_descricao.get()
            imagem = imagem_str

            if imagem == '':
                imagem = e_descricao.insert(0, treev_lista[7])

            lista_atualizar = [nome, autor, isbn, editora, data_da_compra, valor_da_compra, obs, imagem, id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos.')
                    return

            atualizar_dados(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso.')

            e_nome.delete(0, 'end')
            e_autor.delete(0, 'end')
            e_isbn.delete(0, 'end')
            e_editora.delete(0, 'end')
            e_data_compra.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_descricao.delete(0, 'end')

            botao_confirmar.destroy()

            mostrar()
    
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela.')
    
    global botao_confirmar
    botao_confirmar = Button(frameMeio, command=update, image=confirmar_img, width=100, overrelief=RIDGE, text=' Confirmar', height=20, anchor=CENTER, compound=LEFT, font=('Verdana 10 bold'), bg=co4, fg=co1)
    botao_confirmar.place(x=360,y=261)

# ------- FUNÇÃO DELETAR -------
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        deletar_dados([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso.')
         
        mostrar()
        
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela.')

# ------- FUNÇÃO ESCOLHER IMAGEM -------
def escolher_imagem():
    global imagem, imagem_str, label_imagem
    imagem = fd.askopenfilename()
    imagem_str = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((170,244))
    imagem = ImageTk.PhotoImage(imagem)

    label_imagem = Label(frameMeio, image=imagem)
    label_imagem.place(x=670, y=18)

# ------- FUNÇÃO VER IMAGEM -------
def ver_imag():
    global imagem, imagem_str, label_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    iten = ver_item(valor)
    imagem = iten[0][8]

    imagem = Image.open(imagem)
    imagem = imagem.resize((170,244))
    imagem = ImageTk.PhotoImage(imagem)

    label_imagem = Label(frameMeio, image=imagem)
    label_imagem.place(x=670, y=18)

# ------- FUNÇÃO LIMPAR TELA -------
def limpar_tela():
    e_nome.delete(0, 'end')
    e_autor.delete(0, 'end')
    e_isbn.delete(0, 'end')
    e_editora.delete(0, 'end')
    e_data_compra.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_descricao.delete(0, 'end')
    
    label_imagem.destroy()
    botao_confirmar.destroy()
    
# ------- FRAME DE CIMA -------
app_img = Image.open('livro.png')
app_img = app_img.resize((50,50))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text='Inventário de Biblioteca Particular', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 16 bold'), bg=co1, fg=co0)
app_logo.place(x=0, y=0)

# ------- FRAME DO MEIO -------
l_nome = Label(frameMeio, text='Título', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co2)
l_nome.place(x=10, y=20)
e_nome = Entry(frameMeio, width=30, justify=LEFT, relief=SOLID)
e_nome.place(x=135,y=21)

l_autor = Label(frameMeio, text='Autor', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co2)
l_autor.place(x=10, y=60)
e_autor = Entry(frameMeio, width=30, justify=LEFT, relief=SOLID)
e_autor.place(x=135,y=61)

l_isbn = Label(frameMeio, text='ISBN', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co2)
l_isbn.place(x=10, y=100)
e_isbn = Entry(frameMeio, width=30, justify=LEFT, relief=SOLID)
e_isbn.place(x=135,y=101)

l_descricao = Label(frameMeio, text='Gênero literário', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co2)
l_descricao.place(x=10, y=140)
e_descricao = Entry(frameMeio, width=30, justify=LEFT, relief=SOLID)
e_descricao.place(x=135,y=141)

l_editora = Label(frameMeio, text='Editora', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co2)
l_editora.place(x=10, y=180)
e_editora = Entry(frameMeio, width=30, justify=LEFT, relief=SOLID)
e_editora.place(x=135,y=181)

l_data_compra = Label(frameMeio, text='Data da compra', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co2)
l_data_compra.place(x=10, y=220)
e_data_compra = Entry(frameMeio, width=30, justify=LEFT, relief=SOLID)
e_data_compra.place(x=135,y=221)

l_valor = Label(frameMeio, text='Valor', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co2)
l_valor.place(x=10, y=260)
e_valor = Entry(frameMeio, width=30, justify=LEFT, relief=SOLID)
e_valor.place(x=135,y=261)

l_imagem_capa = Label(frameMeio, text='Imagem', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co2)
l_imagem_capa.place(x=10, y=300)
e_imagem_capa = Button(frameMeio, command=escolher_imagem, width=22, overrelief=RIDGE, text='CARREGAR'.upper(), height=1, anchor=CENTER, font=('Verdana 8 bold'), bg=co6, fg=co0)
e_imagem_capa.place(x=135,y=301)

# ------- IMAGENS DOS BOTÕES -------
inserir_img = Image.open('inserir.png')
inserir_img = inserir_img.resize((18,18))
inserir_img = ImageTk.PhotoImage(inserir_img)

editar_img = Image.open('editar.png')
editar_img = editar_img.resize((18,18))
editar_img = ImageTk.PhotoImage(editar_img)

deletar_img = Image.open('deletar.png')
deletar_img = deletar_img.resize((18,18))
deletar_img = ImageTk.PhotoImage(deletar_img)

limpar_img = Image.open('limpar.png')
limpar_img = limpar_img.resize((18,18))
limpar_img = ImageTk.PhotoImage(limpar_img)

confirmar_img = Image.open('confirmar.png')
confirmar_img = confirmar_img.resize((18,18))
confirmar_img = ImageTk.PhotoImage(confirmar_img)

visualizar_img = Image.open('visualizar.png')
visualizar_img = visualizar_img.resize((18,18))
visualizar_img = ImageTk.PhotoImage(visualizar_img)

# ------- BOTÕES -------
botao_inserir = Button(frameMeio, command=inserir, image=inserir_img, width=100, overrelief=RIDGE, text=' Novo', height=20, anchor=CENTER, compound=LEFT, font=('Verdana 10 bold'), bg=co3, fg=co1)
botao_inserir.place(x=360,y=20)

botao_atualizar = Button(frameMeio, command=atualizar, image=editar_img, width=100, overrelief=RIDGE, text=' Editar', height=20, anchor=CENTER, compound=LEFT, font=('Verdana 10 bold'), bg=co4, fg=co1)
botao_atualizar.place(x=360,y=55)

botao_deletar = Button(frameMeio, command=deletar, image=deletar_img, width=100, overrelief=RIDGE, text=' Deletar', height=20, anchor=CENTER, compound=LEFT, font=('Verdana 10 bold'), bg=co5, fg=co1)
botao_deletar.place(x=360,y=125)

botao_visualizar = Button(frameMeio, command=ver_imag, image=visualizar_img, width=100, overrelief=RIDGE, text=' Ver', height=20, anchor=CENTER, compound=LEFT, font=('Verdana 10 bold'), bg=co4, fg=co1)
botao_visualizar.place(x=360,y=296)

botao_limpar = Button(frameMeio, command=limpar_tela, image=limpar_img, width=100, overrelief=RIDGE, text=' Limpar', height=20, anchor=CENTER, compound=LEFT, font=('Verdana 10 bold'), bg=co4, fg=co1)
botao_limpar.place(x=360,y=90)

# ------- VALORES E QUANTIDADE -------
l_total_titulo = Label(frameMeio, text='Valor investido', height=1, anchor=CENTER, font=('Verdana 10 bold'), bg=co1, fg=co0)
l_total_titulo.place(x=507, y=15)
l_total = Label(frameMeio, text='Valor investido', height=1, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co2)
l_total.place(x=508, y=35)

l_qtde_titulo = Label(frameMeio, text='Qtde. de livros', height=1, anchor=CENTER, font=('Verdana 10 bold'), bg=co1, fg=co0)
l_qtde_titulo.place(x=507, y=65)
l_qtde = Label(frameMeio, text='Total de livros', height=1, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co2)
l_qtde.place(x=508, y=85)

l_comprados = Label(frameMeio, text='Comprados', height=1, anchor=CENTER, font=('Verdana 10 bold'), bg=co1, fg=co0)
l_comprados.place(x=507, y=115)
l_comprados_ = Label(frameMeio, text='Aqui', height=1, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co2)
l_comprados_.place(x=508, y=135)

l_ganhados = Label(frameMeio, text='Ganhados', height=1, anchor=CENTER, font=('Verdana 10 bold'), bg=co1, fg=co0)
l_ganhados.place(x=507, y=165)
l_ganhados_ = Label(frameMeio, text='Aqui', height=1, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co2)
l_ganhados_.place(x=508, y=185)

# ------- FRAME DE BAIXO / TABELA -------
def mostrar():
    global tree
    tabela_head = ['ID','Título','Autor','ISBN', 'Editora', 'Data','Valor', 'Gênero']
    lista_itens = ver_livros()
    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,150,100,140,80,80,140]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

    quantidade = []
    quant_comprados = []
    quant_ganhados = []

    for iten in lista_itens:
        quantidade.append(iten[6])
        if iten[6] != 0:
            quant_comprados.append(iten[6])
        else:
            quant_ganhados.append(iten[6])

    total_valor = sum(quantidade)
    total_itens = len(quantidade)

    total_com_valor = len(quant_comprados)
    total_sem_valor = len(quant_ganhados)

    l_total['text'] = 'R$ {:,.2f}'.format(total_valor)
    l_qtde['text'] = total_itens
    l_comprados_['text'] = total_com_valor
    l_ganhados_['text'] = total_sem_valor

mostrar()

janela.mainloop()
