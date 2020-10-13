import tkinter as tk
from tkinter import *
from tkinter import messagebox

def limpaLabel(string, tam):
    nstring = ""
    i = 0
    letter = string.split()
    while i < tam:
        nstring += letter[i] + " "
        i += 1
    return nstring        


def LimpaCaixa():
    ResultBox['text'] = limpaLabel(ResultBox['text'],lenR)

def FechaJanela():
    janela.destroy()

def PressButton():
    ResultBox['text'] = limpaLabel(ResultBox['text'],lenR)
    try:
        n1 = float(TextBox1.get())
        n2 = float(TextBox2.get())
        if status1.get() == 1:
            resul = n1 + n2
            ResultBox['text'] = ResultBox['text'] + str(resul)
        if status1.get() == 3:
            resul = n1 - n2
            ResultBox['text'] = ResultBox['text'] + str(resul)
        if status1.get() == 5:
            resul = n1 * n2
            ResultBox['text'] = ResultBox['text'] + str(resul)
        if status1.get() == 7:
            if n2 == 0:
                messagebox.showinfo("ERROR", "ERROR 02: INDIVISÍVEL POR ZERO!")
            else:   
                resul = n1 / n2
                ResultBox['text'] = ResultBox['text'] + str(resul)
    except:
        messagebox.showinfo("ERROR", "ERROR 01: ENTRADA INVÁLIDA!")
    TextBox1.delete(0, END)
    TextBox2.delete(0, END)
    
    
janela = Tk()
janela.title('Calculadora v1.1')

TextBox1 = Entry(janela, background = 'gray' ,width = 16, font = 'Arial18', bg = 'white')
TextBox1.place(x=18,y=65)
TextBox2 = Entry(janela, background = 'gray' ,width = 16, font = 'Arial18', bg = 'white')
TextBox2.place(x=192,y=65)

status1 = IntVar()
label1 = Label(janela, text='+', font = 'Arial 12', bg = '#4B0082', fg = 'white')
label1.place(x=173,y=66)
ResultBox = Label(janela, text='A Soma é -> ', font = 'Arial 12', bg = '#4B0082', fg = 'white') 
ResultBox.place(x=22,y=125)
splR  = ResultBox['text'].split()
lenR = len(splR)
def labSum():
    label1['text'] = '+'
    label1['font'] = 'Arial 12'
    ResultBox['text'] = 'A Soma é -> '
    splR  = ResultBox['text'].split()
    lenR = len(splR)

def labDif():
    label1['text'] = '-'
    label1['font'] = 'Arial 18'
    ResultBox['text'] = 'A Diferença é -> '
    splR  = ResultBox['text'].split()
    lenR = len(splR)

def labProd():
    label1['text'] = '*'
    label1['font'] = 'Arial 15'
    ResultBox['text'] = 'O Produto é -> '
    splR  = ResultBox['text'].split()
    lenR = len(splR)

def labQuo():
    label1['text'] = '/'
    label1['font'] = 'Arial 15'
    ResultBox['text'] = 'O Quociente é -> '
    splR  = ResultBox['text'].split()
    lenR = len(splR)

CheckBox1 = Checkbutton(janela, text='Adição', variable=status1, onvalue=1, offvalue=0, selectcolor = '#008080' , bg = '#4B0082', fg = 'white', command = labSum)
CheckBox1.select()
CheckBox1.pack()
CheckBox1.place(x=25,y=25)

CheckBox2 = Checkbutton(janela, text='Subtração', variable=status1, onvalue=3, offvalue=2, selectcolor = '#008080' , bg = '#4B0082', fg = 'white', command = labDif)
CheckBox2.pack()
CheckBox2.place(x=90,y=25)

CheckBox3 = Checkbutton(janela, text='Multiplicação', variable=status1, onvalue=5, offvalue=4, selectcolor = '#008080' , bg = '#4B0082', fg = 'white', command = labProd)
CheckBox3.pack()
CheckBox3.place(x=173,y=25)

CheckBox4 = Checkbutton(janela, text='Divisão', variable=status1, onvalue=7, offvalue=6, selectcolor = '#008080' , bg = '#4B0082', fg = 'white', command = labQuo)
CheckBox4.pack()
CheckBox4.place(x=273,y=25)

btn = Button(janela, width = 25, text = 'CALCULAR', command = PressButton, background = 'blue', fg = 'white')
btn.place(x=75,y=165)

btnLimpa = Button(janela, width = 15, text = 'LIMPAR', command = LimpaCaixa, background = 'green', fg = 'white')
btnLimpa.place(x=10,y=225)

btnFecha = Button(janela, width = 15, text = 'FECHAR', command = FechaJanela, background = 'red', fg = 'white')
btnFecha.place(x=215,y=225)

janela.geometry('360x280+250+100')
janela.configure(bg='#4B0082')
janela.resizable(0,0)
janela.mainloop()
