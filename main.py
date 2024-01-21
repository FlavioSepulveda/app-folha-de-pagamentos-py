# Criando aplicação python pra gerenciamento de pagamentos 
from tkinter import *
from tkinter import ttk, messagebox
import os
import locale
# DEFININDO A LOCALIZAÇÃO
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Cores usadas -------------------------------------------
cor0 = "#595959"
corFundo1 = "#ECE9E2"
corFundo2 = "#595959"
corLetras = "#403d3d"

# Criando janela da aplicação ----------------------------
janela = Tk() # Cria uma janela visualmente agradavel.
janela.title("Folha de pagamentos") # Cria o titulo da janela
janela.geometry('490x610') # Da a janela as dimensões
janela.configure(background = corFundo1)
janela.resizable(width = FALSE, height=FALSE)

# Frames principais --------------------------------------
frameCima = Frame(janela, width=500, height=70, bg= corFundo1, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky = NSEW)

frameMeio = Frame(janela, width=500, height=300, bg= corFundo1, relief="solid")
frameMeio.grid(row=1, column=0, sticky = NSEW)
frameMeio_H = Frame(frameMeio, width=500, height=50, bg= corFundo1, relief="solid")
frameMeio_H.grid(row=0, column=0, sticky = NSEW)
frameMeio_B = Frame(frameMeio, width=500, height=200, bg= corFundo1, relief="solid")
frameMeio_B.grid(row=1, column=0, sticky = NSEW)

frameBaixo = Frame(janela, width=500, height=150, bg= corFundo1, relief="raised")
frameBaixo.grid(row=2, column=0,pady=10, sticky = NSEW)
frameBaixo_P = Frame(frameBaixo, width=500, height=100, bg= corFundo1, relief="raised")
frameBaixo_P.grid(row=0, column=0, sticky = NSEW)
frameBaixo_D = Frame(frameBaixo, width=500, height=100, bg= corFundo1, relief="raised")
frameBaixo_D.grid(row=1, column=0, sticky = NSEW)

frameBaixo_S = Frame(frameBaixo, width=500, height=100, bg= corFundo1, relief="raised")
frameBaixo_S.grid(row=2, column=0, sticky = NSEW)

frameMenu = Frame(janela, width=50, height=150, bg= corFundo1, relief="raised")
frameMenu.grid(row=3, column=0, sticky = NSEW)

# Frame cima --------------------------------------------
app_logo = Label(frameCima, text="Folha de pagamento", compound=LEFT, padx=5, anchor= NW, font=("Arial 20"), bg=corFundo1, fg=corFundo2)
app_logo.place(x=10,y=20)

# Frame meio --------------------------------------------
app_label = Label(frameMeio_H, text="Dados do Trabalhador", compound=LEFT, padx=5, anchor= NW, font=("Arial 13"), bg=corFundo1, fg=cor0)
app_label.place(x=10,y=7)

app_linha = Label(frameMeio_H, width=270,anchor= NW, font=("Verdana 1"), bg=cor0)
app_linha.place(x=190,y=17)
app_linha = Label(frameMeio_H, width=270,anchor= NW, font=("Verdana 1"), bg=corFundo1)
app_linha.place(x=190,y=19)

l_nome = Label(frameMeio_B, text="Nome*", anchor= NW, font=("Ivy 10"), bg=corFundo1, fg=corLetras)
l_nome.grid(row=0, column=0,pady=5, padx=20, sticky = NSEW)
e_nome = Entry(frameMeio_B, width=25, justify='left', relief='solid')
e_nome.grid(row=0, column=1,pady=5, sticky = NSEW)

l_cpf = Label(frameMeio_B, text="CPF*", anchor= NW, font=("Ivy 10"), bg=corFundo1, fg=corLetras)
l_cpf.grid(row=1, column=0,pady=5, padx=20, sticky = NSEW)
e_cpf = Entry(frameMeio_B, width=25, justify='left', relief='solid')
e_cpf.grid(row=1, column=1,pady=5, sticky = NSEW)

l_cargo = Label(frameMeio_B, text="Cargo*", anchor= NW, font=("Ivy 10"), bg=corFundo1, fg=corLetras)
l_cargo.grid(row=2, column=0,pady=5, padx=20, sticky = NSEW)
e_cargo = Entry(frameMeio_B, width=25, justify='left', relief='solid')
e_cargo.grid(row=2, column=1,pady=5, sticky = NSEW)

l_salario = Label(frameMeio_B, text="Salario Bruto*", anchor= NW, font=("Ivy 10"), bg=corFundo1, fg=corLetras)
l_salario.grid(row=3, column=0,pady=5, padx=20, sticky = NSEW)
e_salario = Entry(frameMeio_B, width=25, justify='center', relief='solid')
e_salario.grid(row=3, column=1,pady=5, sticky = NSEW)

l_horas = Label(frameMeio_B, text="Horas*", anchor= NW, font=("Ivy 10"), bg=corFundo1, fg=corLetras)
l_horas.grid(row=3, column=2,pady=5, padx=20, sticky = NSEW)
e_horas = Entry(frameMeio_B, width=8, justify='center', relief='solid')
e_horas.grid(row=3, column=3,pady=5, sticky = NSEW)

# Frame Baixo ----------------------------------------------
app_label = Label(frameBaixo_P, text="Proventos", compound=LEFT, padx=5, anchor= NW, font=("Arial 13"), bg=corFundo1, fg=cor0)
app_label.place(x=10,y=7)

app_linha = Label(frameBaixo_P, width=360,anchor= NW, font=("Verdana 1"), bg=cor0)
app_linha.place(x=100,y=18)
app_linha = Label(frameBaixo_P, width=360,anchor= NW, font=("Verdana 1"), bg=corFundo1)
app_linha.place(x=100,y=20)

l_salario = Label(frameBaixo_P, text="Salario Bruto: ", compound=LEFT, padx=5, anchor= NW, font=("Arial 10"), bg=corFundo1, fg=corLetras)
l_salario.place(x=20,y=40)
app_salario = Label(frameBaixo_P, text=locale.currency(5000, grouping=TRUE),  compound=LEFT, padx=5, anchor= NW, font=("Arial 10 bold"), bg=corFundo1, fg=corLetras)
app_salario.place(x=150,y=40)

l_horasExtras = Label(frameBaixo_P, text="Horas Extras: ", compound=LEFT, padx=5, anchor= NW, font=("Arial 10"), bg=corFundo1, fg=corLetras)
l_horasExtras.place(x=20,y=60)
app_horasExtras= Label(frameBaixo_P, text=locale.currency(00, grouping=TRUE),  compound=LEFT, padx=5, anchor= NW, font=("Arial 10 bold"), bg=corFundo1, fg=corLetras)
app_horasExtras.place(x=150,y=60)

# Frame de descontos -------------------------------------
app_label = Label(frameBaixo_D, text="Descontos", compound=LEFT, padx=5, anchor= NW, font=("Arial 13"), bg=corFundo1, fg=cor0)
app_label.place(x=10,y=7)

app_linha = Label(frameBaixo_D, width=360,anchor= NW, font=("Verdana 1"), bg=cor0)
app_linha.place(x=100,y=18)
app_linha = Label(frameBaixo_D, width=360,anchor= NW, font=("Verdana 1"), bg=corFundo1)
app_linha.place(x=100,y=20)

l_INSS = Label(frameBaixo_D, text="INSS: ", compound=LEFT, padx=5, anchor= NW, font=("Arial 10"), bg=corFundo1, fg=corLetras)
l_INSS.place(x=20,y=40)
app_INSS = Label(frameBaixo_D, text=locale.currency(5000, grouping=TRUE),  compound=LEFT, padx=5, anchor= NW, font=("Arial 10 bold"), bg=corFundo1, fg=corLetras)
app_INSS.place(x=150,y=40)

l_IRRF = Label(frameBaixo_D, text="IRRF: ", compound=LEFT, padx=5, anchor= NW, font=("Arial 10"), bg=corFundo1, fg=corLetras)
l_IRRF.place(x=20,y=60)
app_IRRF = Label(frameBaixo_D, text=locale.currency(00, grouping=TRUE),  compound=LEFT, padx=5, anchor= NW, font=("Arial 10 bold"), bg=corFundo1, fg=corLetras)
app_IRRF.place(x=150,y=60)

l_IRRF = Label(frameBaixo_S, text="Liquido a receber: ", compound=LEFT, padx=5, anchor= NW, font=("Arial 12"), bg=corFundo1, fg=corLetras)
l_IRRF.place(x=20,y=7)
app_linha = Label(frameBaixo_S, width=300,anchor= NW, font=("Verdana 1"), bg=cor0)
app_linha.place(x=160,y=18)
app_linha = Label(frameBaixo_S, width=300,anchor= NW, font=("Verdana 1"), bg=corFundo1)
app_linha.place(x=160,y=20)

app_salario_receber = Label(frameBaixo_S, width=18, text=locale.currency(00, grouping=TRUE),  compound=LEFT, padx=5, anchor= E, font=("Arial 20 bold"), bg=corFundo1, fg=corLetras)
app_salario_receber.place(x=150,y=40)

# Menu --------------------------------------------
b_folha_pagamento = Button(frameMenu, anchor=NW, text='Calcular Pagamento', bg=corLetras,fg=corFundo1, font=('Ivy 10 bold'), overrelief=RIDGE, relief=GROOVE)
b_folha_pagamento.grid(row=0, column=0, sticky=NSEW,padx=10, pady=6)

b_folha_pagamento = Button(frameMenu, anchor=NW, text='Gerar PDF', bg=corLetras,fg=corFundo1, font=('Ivy 10 bold'), overrelief=RIDGE, relief=GROOVE)
b_folha_pagamento.grid(row=0, column=2, sticky=NSEW,padx=10, pady=6)

janela.mainloop()