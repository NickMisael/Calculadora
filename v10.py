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
                messagebox.showinfo("Error", "Error 02: indivisivel por zero!")
            else:   
                resul = n1 / n2
                ResultBox['text'] = ResultBox['text'] + str(resul)
    except:
        messagebox.showinfo("Error", "Error 01: Entrada invalida!")
    TextBox1.delete(0, END)
    TextBox2.delete(0, END)
    
    
janela = Tk()
janela.title('Calculadora v1.1')

TextBox1 = Entry(janela, background = 'gray' ,width = 10, font = 'Arial18')
TextBox1.place(x=210,y=100)
TextBox2 = Entry(janela, background = 'gray' ,width = 10, font = 'Arial18')
TextBox2.place(x=337,y=100)

status1 = IntVar()
label1 = Label(janela, text='+', font = 'Arial 12')
label1.place(x=318,y=100)
ResultBox = Label(janela, text='A soma eh: ', font = 'Arial 12') 
ResultBox.place(x=212,y=150)
splR  = ResultBox['text'].split()
lenR = len(splR)
def labSum():
    label1['text'] = '+'
    ResultBox['text'] = 'A soma eh: '
    splR  = ResultBox['text'].split()
    lenR = len(splR)

def labDif():
    label1['text'] = '-'
    ResultBox['text'] = 'A diferenca eh: '
    splR  = ResultBox['text'].split()
    lenR = len(splR)

def labProd():
    label1['text'] = '*'
    ResultBox['text'] = 'O produto eh: '
    splR  = ResultBox['text'].split()
    lenR = len(splR)

def labQuo():
    label1['text'] = '/'
    ResultBox['text'] = 'O quociente eh: '
    splR  = ResultBox['text'].split()
    lenR = len(splR)

CheckBox1 = Checkbutton(janela, text='Adicao', variable=status1, onvalue=1, offvalue=0, command = labSum)
CheckBox1.select()
CheckBox1.pack()
CheckBox1.place(x=210,y=75)

CheckBox2 = Checkbutton(janela, text='Subtracao', variable=status1, onvalue=3, offvalue=2, command = labDif)
CheckBox2.pack()
CheckBox2.place(x=275,y=75)

CheckBox3 = Checkbutton(janela, text='Multiplicacao', variable=status1, onvalue=5, offvalue=4, command = labProd)
CheckBox3.pack()
CheckBox3.place(x=355,y=75)

CheckBox4 = Checkbutton(janela, text='Divisao', variable=status1, onvalue=7, offvalue=6, command = labQuo)
CheckBox4.pack()
CheckBox4.place(x=450,y=75)

btn = Button(janela, width = 25, text = 'Calcular', command = PressButton, background = 'blue')
btn.place(x=205,y=175)

janela.geometry('640x480+250+100')
janela.mainloop()
