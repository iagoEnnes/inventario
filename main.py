from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
from view import *
from tkinter import filedialog as fd

l_imagem = None


#Criando Janela
Janela = Tk()
Janela.title('')
Janela.geometry('900x600')
Janela.configure(background="#1e1e1f")
Janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(Janela)
style.theme_use("clam")


#FramesCima
frameCima = Frame(Janela, width=1043, height=43, bg="#c7c9c9", relief=FLAT)
frameCima.grid(row=0, column=0)

#FrameMeio
frameMeio = Frame(Janela, width=1043, height=303, bg="#64bfed", pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#FrameBaixo
frameBaixo = Frame(Janela, width=1043, height=300, bg="#ffffff", relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

#Funções---------------------------------------------------------------------------------------------------------------------
global tree

#InserirDados---------------------------------------------------------------------------------------------------------------------
def inserir():
    global imagem, imagem_string, l_imagem
    
    nome = e_nome.get()
    Item = e_Item.get()
    Quantia = e_Quantia.get()
    Data = e_Data.get()
    Descricao = e_Descricao.get()
    imagem = imagem_string

    lista_inserir = [nome, Item, Quantia, Data, Descricao, imagem]

    for i in lista_inserir:
        if i =='':
            messagebox.showerror('Erro','Falta campos a serem preenchidos.')
            return

    inserir_formulario(lista_inserir)
    messagebox.showinfo('Sucesso','Item Registrado sem falhas.')
    e_nome.delete(0,'end')
    e_Item.delete(0,'end')
    e_Quantia.delete(0,'end')
    e_Descricao.delete(0,'end')
    e_Data.delete(0,'end')


    mostrar()

#AtualizarDados---------------------------------------------------------------------------------------------------------------------
def atualizar_dados():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        # Use a ordem correta para os campos
        id = int(treev_lista[0])
        e_nome.delete(0, 'end')
        e_Item.delete(0, 'end')
        e_Quantia.delete(0, 'end')
        e_Data.delete(0, 'end')
        e_Descricao.delete(0, 'end')

        e_nome.insert(0, treev_lista[1])
        e_Item.insert(0, treev_lista[2])
        e_Quantia.insert(0, treev_lista[3])
        e_Data.insert(0, treev_lista[4])         # Data vem antes de Descrição
        e_Descricao.insert(0, treev_lista[5])    # Descrição vem depois de Data
        imagem_string = treev_lista[6]

        def update():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            Item = e_Item.get()
            Quantia = e_Quantia.get()
            Data = e_Data.get()
            Descricao = e_Descricao.get()
            imagem = imagem_string

            lista_atualizar = [nome, Item, Quantia, Data, Descricao, imagem, id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro', 'Falta campos a serem preenchidos.')
                    return

            atualizar_formulario(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Item atualizado sem falhas.')
            e_nome.delete(0, 'end')
            e_Item.delete(0, 'end')
            e_Quantia.delete(0, 'end')
            e_Data.delete(0, 'end')
            e_Descricao.delete(0, 'end')

            b_Confirmar.destroy()
            mostrar()

        b_Confirmar = Button(frameMeio, command=update, width=13, text='CONFIRMAR', overrelief=RIDGE, font=('Ivy 8 bold'), bg='#ffffff', fg='#000000')
        b_Confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror('Erro.', 'Selecione um dos dados na tabela.')

l_imagem = None  # Inicializa como None para indicar que não há imagem carregada


#DeletarDados---------------------------------------------------------------------------------------------------------------------
def Deletar_dados():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_formulario([valor])

        messagebox.showinfo('Sucesso','Item deletados sem falhas.')

        mostrar()
            
    except IndexError:
        messagebox.showerror('Erro.','Selecione um dos dados na tabela.')



#CarregarImagem---------------------------------------------------------------------------------------------------------------------
def escolherImagem():
    global imagem, imagem_string, l_imagem
    limpar_imagem()  # Limpa a imagem anterior
    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((250, 250))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg="#c7c9c9", fg="#000000")
    l_imagem.place(x=550, y=10)

#VerImagem---------------------------------------------------------------------------------------------------------------------
def ver_imagem():
    global imagem, imagem_string, l_imagem
    limpar_imagem()  # Limpa a imagem anterior

    # Obter o item selecionado na árvore
    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]
    item = ver_item(valor)

    # Carregar e redimensionar a imagem
    imagem_path = item[0][6]
    imagem = Image.open(imagem_path)
    imagem = imagem.resize((250, 250))
    imagem = ImageTk.PhotoImage(imagem)

    # Criar e posicionar o Label para a imagem
    l_imagem = Label(frameMeio, image=imagem, bg="#c7c9c9", fg="#000000")
    l_imagem.image = imagem  # Armazena a referência da imagem no Label
    l_imagem.place(x=550, y=10)

    # Atualizar o frame para aplicar as mudanças
    frameMeio.update()

#CamposCima
#AbrindoImagem
app_img = Image.open('IconeInventario.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Inventário do Almoxarifado', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 15 bold'), bg="#c7c9c9", fg="#000000")
app_logo.place(x=0, y=-4)

#CamposMeio

#Entradas
#REGISTRAR O NOME-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#64bfed', fg='#000000')
l_nome.place(x=20, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=90, y=11)

#REGISTRAR O ITEM-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
l_Item = Label(frameMeio, text='Item', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#64bfed', fg='#000000')
l_Item.place(x=20, y=40)
e_Item = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_Item.place(x=90, y=41)

#REGISTRAR A QUANTIDADE----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
l_Quantia = Label(frameMeio, text='Quantia', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#64bfed', fg='#000000')
l_Quantia.place(x=20, y=70)
e_Quantia = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_Quantia.place(x=90, y=71)

#REGISTRAR A DESCRIÇÃO----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
l_Descricao = Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#64bfed', fg='#000000')
l_Descricao.place(x=20, y=100)
e_Descricao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_Descricao.place(x=90, y=101)

#REGISTRAR A DATA---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
l_Data = Label(frameMeio, text='Data', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#64bfed', fg='#000000')
l_Data.place(x=20, y=130)
e_Data = DateEntry(frameMeio, width=12, background ='#64bfed'  , bordewidht = 2, year =2024, date_pattern='dd/MM/yyyy')
e_Data.place(x=90, y=131)

#BOTÃO DE CARREGAR IMAGEM---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
b_Imagem = Label(frameMeio, text='Imagem', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#64bfed', fg='#000000')
b_Imagem.place(x=20, y=160)
b_Imagem = Button(frameMeio, command=escolherImagem, text='Carregar', width=29, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg='#ffffff', fg='#000000')
b_Imagem.place(x=90, y=161)

#BOTÃO DE INSERIR DADO---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Imagem_Inserir = Image.open('IconeInserir.png')
Imagem_Inserir = Imagem_Inserir.resize((20,20))
Imagem_Inserir = ImageTk.PhotoImage(Imagem_Inserir)

b_InserirDado = Button(frameMeio,command=inserir, image=Imagem_Inserir, text='  ADICIONAR', width=95, compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg='#ffffff', fg='#000000')
b_InserirDado.place(x=330, y=10)

#BOTÃO DE ATUALIZAR------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Imagem_Atualizar = Image.open('Atualizar.png')
Imagem_Atualizar = Imagem_Atualizar.resize((20,20))
Imagem_Atualizar = ImageTk.PhotoImage(Imagem_Atualizar)

b_AtualizarDado = Button(frameMeio,command=atualizar_dados, image=Imagem_Atualizar, text='  ATUALIZAR', width=95, compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg='#ffffff', fg='#000000')
b_AtualizarDado.place(x=330, y=50)

#BOTÃO DE DELETAR---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Imagem_Deletar = Image.open('Deletar.png')
Imagem_Deletar = Imagem_Deletar.resize((20,20))
Imagem_Deletar = ImageTk.PhotoImage(Imagem_Deletar)

b_DeletarDado = Button(frameMeio, command=Deletar_dados, image=Imagem_Deletar, text='  DELETAR', width=95, compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg='#ffffff', fg='#000000')
b_DeletarDado.place(x=330, y=90)

#BOTÃO DE VISUALIZAR IMAGEM------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Imagem_Visualizar = Image.open('Visualizar.png')
Imagem_Visualizar = Imagem_Visualizar.resize((20,20))
Imagem_Visualizar = ImageTk.PhotoImage(Imagem_Visualizar)

b_DeletarDado = Button(frameMeio,command=ver_imagem, image=Imagem_Visualizar, text='  VISUALIZAR', width=95, compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg='#ffffff', fg='#000000')
b_DeletarDado.place(x=330, y=130)

#---------------------------------------------------------------------------------------------------------------------

def mostrar():
    global tree

    #Scroll Bars
    tabela_head = ['#Item', 'Nome', 'Item','Quantia', 'Data', 'Descrição']

    lista_itens = ver_formulario()


    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center",'center']
    h=[50,100,100,100,130,401]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    #inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


mostrar()


Janela.mainloop()