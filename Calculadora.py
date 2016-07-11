#!/usr/bin/env python3

import tkinter

# Funções

def sair():
    window.destroy()

# Arrumar, pois está inserindo a esquerda
def pressb1():
    visor.insert(0, "1")

def pressb2():
    visor.insert(0, "2")

def pressb3():
    visor.insert(0, "3")

def pressb4():
    visor.insert(0, "4")

def pressb5():
    visor.insert(0, "5")

def pressb6():
    visor.insert(0, "6")

def pressb7():
    visor.insert(0, "7")

def pressb8():
    visor.insert(0, "8")

def pressb9():
    visor.insert(0, "9")

def pressblimpa():
    visor.delete(0)

# Criando a janela
window=tkinter.Tk()

window.title("Calculadora 0.0")
window.geometry("270x300")

# Colocando o menu (não está funcionando)

# Criando o corpo de operações
esp1 = tkinter.Label(window, text="")
esp1.pack()

visor = tkinter.Entry(window, width=24)
visor.pack()

esp2 = tkinter.Label(window, text="")
esp2.pack()

num = tkinter.Frame(window)
num.pack()

b1 = tkinter.Button(num, text="1", width=3, command=pressb1).grid(row=1,column=0)
b2 = tkinter.Button(num, text="2", width=3, command=pressb2).grid(row=1,column=1)
b3 = tkinter.Button(num, text="3", width=3, command=pressb3).grid(row=1,column=2)
bsoma = tkinter.Button(num, text="+", width=3).grid(row=1,column=3)
b4 = tkinter.Button(num, text="4", width=3, command=pressb4).grid(row=2,column=0)
b5 = tkinter.Button(num, text="5", width=3, command=pressb5).grid(row=2,column=1)
b6 = tkinter.Button(num, text="6", width=3, command=pressb6).grid(row=2,column=2)
bsub = tkinter.Button(num, text="-", width=3).grid(row=2,column=3)
b7 = tkinter.Button(num, text="7", width=3, command=pressb7).grid(row=3,column=0)
b8 = tkinter.Button(num, text="8", width=3, command=pressb8).grid(row=3,column=1)
b9 = tkinter.Button(num, text="9", width=3, command=pressb9).grid(row=3,column=2)
bmult = tkinter.Button(num, text="x", width=3).grid(row=3,column=3)
blimpa = tkinter.Button(num, text="C", width=3, command=pressblimpa).grid(row=4,column=0)
zero = tkinter.Button(num, text="0", width=3).grid(row=4,column=1)
bponto = tkinter.Button(num, text=".", width=3).grid(row=4,column=2)
bdiv = tkinter.Button(num, text="/", width=3).grid(row=4,column=3)

bresul = tkinter.Button(window, text="=", width=7)
bresul.pack()

esp4 = tkinter.Label(window, text="")
esp4.pack()

quitb = tkinter.Button(window, text="Sair", command=sair)
quitb.pack()

window.mainloop()
