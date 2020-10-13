import tkinter as tk
from tkinter import *

def limpaLabel(string, tam):
    nstring = ""
    i = 0
    letter = string.split()
    while i < tam:
        nstring += letter[i] + " "
        i += 1
    return nstring        
    

def PressButton():
    soma['text'] = limpaLabel(soma['text'],lenS)
    dif['text'] = limpaLabel(dif['text'],lenD)  
    prod['text'] = limpaLabel(prod['text'],lenP)
    quoc['text'] = limpaLabel(quoc['text'],lenQ) 
    try:
        n1 = float(TextBox1.get())
        n2 = float(TextBox2.get())
        n3 = float(TextBox3.get())
        n4 = float(TextBox4.get())
        n5 = float(TextBox5.get())
        n6 = float(TextBox6.get())
        n7 = float(TextBox7.get())
        n8 = float(TextBox8.get())
        
        resul = n1 + n2
        soma['text'] = soma['text'] + str(resul)
        resul = n3 - n4
        dif['text'] = dif['text'] + str(resul)
        resul = n5 * n6
        prod['text'] = prod['text'] + str(resul)
        resul = n7 / n8
        quoc['text'] = quoc['text'] + str(resul)
    except:
        errorMsg = Label(janela, text='Error: Entrada invalida!', font = 'Arial 12')
        errorMsg.place(x=215,y=400)
    TextBox1.delete(0,last = None)
    TextBox2.delete(0,last = None)
    TextBox3.delete(0,last = None)
    TextBox4.delete(0,last = None)
    TextBox5.delete(0,last = None)
    TextBox6.delete(0,last = None)
    TextBox7.delete(0,last = None)
    TextBox8.delete(0,last = None)
    
janela = Tk()
janela.title = 'Calculadora v1.0'

TextBox1 = Entry(janela, background = 'gray' ,width = 10, font = 'Arial18')
TextBox1.place(x=210,y=100)
label1 = Label(janela, text='+', font = 'Arial 12')
label1.place(x=320,y=100)
TextBox2 = Entry(janela, background = 'gray' ,width = 10, font = 'Arial18')
TextBox2.place(x=337,y=100)
TextBox3 = Entry(janela, background = 'gray' ,width = 10, font = 'Arial18')
TextBox3.place(x=210,y=150)
label2 = Label(janela, text='-', font = 'Arial 12')
label2.place(x=320,y=150)
TextBox4 = Entry(janela, background = 'gray' ,width = 10, font = 'Arial18')
TextBox4.place(x=337,y=150)
TextBox5 = Entry(janela, background = 'gray' ,width = 10, font = 'Arial18')
TextBox5.place(x=210,y=200)
label3 = Label(janela, text='*', font = 'Arial 12')
label3.place(x=320,y=200)
TextBox6 = Entry(janela, background = 'gray' ,width = 10, font = 'Arial18')
TextBox6.place(x=337,y=200)
TextBox7 = Entry(janela, background = 'gray' ,width = 10, font = 'Arial18')
TextBox7.place(x=210,y=250)
label4 = Label(janela, text='/', font = 'Arial 12')
label4.place(x=320,y=250)
TextBox8 = Entry(janela, background = 'gray' ,width = 10, font = 'Arial18')
TextBox8.place(x=337,y=250)

soma = Label(janela, text='A soma eh: ', font = 'Arial 12') 
soma.place(x=215,y=300)
splS  = soma['text'].split()
lenS = len(splS)

dif = Label(janela, text='A diferenca eh: ', font = 'Arial 12') 
dif.place(x=215,y=320)
splD = dif['text'].split()
lenD = len(splD)

prod = Label(janela, text='O produto eh: ', font = 'Arial 12') 
prod.place(x=215,y=340)
splP = prod['text'].split()
lenP = len(splP)

quoc = Label(janela, text='O quociente eh: ', font = 'Arial 12') 
quoc.place(x=215,y=360)
splQ = quoc['text'].split()
lenQ = len(splQ)

btn = Button(janela, width = 25, text = 'Calcular', command = PressButton, background = 'blue')
btn.place(x=205,y=385)

janela.geometry('640x480+250+100')
janela.mainloop()