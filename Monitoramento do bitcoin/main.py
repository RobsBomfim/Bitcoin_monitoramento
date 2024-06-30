import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

#importando bibliotecas 

import requests
import json

#cores 
color_1 = "#444466" #black
color_2 = "#feffff" #branco
color_3 = "#6f9fbd" #azul

background = "#484f60"

#criando janela
janela = Tk()
janela.title("")
janela.resizable(width=FALSE, height=FALSE)
janela.geometry("340x350")
janela.config(bg=background)

#dividindo a tela em dois frames


ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1 , ipadx=157)

frame_1 = Frame(janela, width=340, height=50, bg=color_1, pady=0, padx=0, relief="flat")
frame_1.grid(row=1,column=0)

frame_2 = Frame(janela, width=340, height=300, bg=background , pady=0, padx=0, relief="flat")
frame_2.grid(row=2,column=0, sticky=NW)


#função para pegar dados

def info():

    link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CAOA%2CBRL'

        #http request
    response = requests.get(link)

        #convertendo  os dados em dicionario
    dados = response.json()

        # valores usd
    valor_usd = float(dados['USD'])
    valor_formatado_usd = '$ {:,.3f}'.format(valor_usd)
    l_p_usd['text'] = valor_formatado_usd

    # valores euro
    valor_euro = float(dados['EUR'])
    valor_formatado_euro = '€ {:,.3f}'.format(valor_euro)
    l_p_euro['text'] = 'Em Euros:' + valor_formatado_euro

    # valores reais
    valor_reais = float(dados['BRL'])
    valor_formatado_reais = 'R$ {:,.3f}'.format(valor_reais)
    l_p_reais['text'] = 'Em Reais:' + valor_formatado_reais

    frame_2.after(1000,info)



#configurando fram_1
imagem = Image.open('bitcoin.png')
imagem = imagem.resize((30,30))
imagem = ImageTk.PhotoImage(imagem)

l_icon =Label(frame_1, image=imagem, compound=LEFT, bg=background, relief=FLAT)
l_icon.place(x=10, y=10)

l_nome =Label(frame_1, text='Monitoramento Bitcoin', bg=color_1 , fg=color_2, relief=FLAT, anchor='center', font=("arial 20"))
l_nome.place(x=50, y=5)

#configurando frame_2
l_p_usd =Label(frame_2, text= '',  bg=background, fg=color_2, relief=FLAT, anchor='center', font=("arial 20"))
l_p_usd.place(x=10, y=50)

l_p_euro =Label(frame_2, text='',  bg=background, fg=color_2, relief=FLAT, anchor='center', font=("arial 12"))
l_p_euro.place(x=10, y=130)

l_p_reais =Label(frame_2, text='',  bg=background, fg=color_2, relief=FLAT, anchor='center', font=("arial 12"))
l_p_reais.place(x=10, y=160)


info()

janela.mainloop()