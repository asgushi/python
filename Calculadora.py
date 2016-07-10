#!/usr/bin/env python3

import tkinter

def sair():
    window.destroy()

window=tkinter.Tk()

window.title("Calculadora 0.0")
window.geometry("270x300")

esp1 = tkinter.Label(window, text="")
esp1.pack()

visor = tkinter.Entry(window, width=24)
visor.pack()

esp2 = tkinter.Label(window, text="")
esp2.pack()

num = tkinter.Frame(window)
num.pack()

b1 = tkinter.Button(num, text="1", width=3).grid(row=1,column=0)
b2 = tkinter.Button(num, text="2", width=3).grid(row=1,column=1)
b3 = tkinter.Button(num, text="3", width=3).grid(row=1,column=2)
bsoma = tkinter.Button(num, text="+", width=3).grid(row=1,column=3)
b4 = tkinter.Button(num, text="4", width=3).grid(row=2,column=0)
b5 = tkinter.Button(num, text="5", width=3).grid(row=2,column=1)
b6 = tkinter.Button(num, text="6", width=3).grid(row=2,column=2)
bsub = tkinter.Button(num, text="-", width=3).grid(row=2,column=3)
b7 = tkinter.Button(num, text="7", width=3).grid(row=3,column=0)
b8 = tkinter.Button(num, text="8", width=3).grid(row=3,column=1)
b9 = tkinter.Button(num, text="9", width=3).grid(row=3,column=2)
bmult = tkinter.Button(num, text="x", width=3).grid(row=3,column=3)
blimpa = tkinter.Button(num, text="C", width=3).grid(row=4,column=0)
zero = tkinter.Button(num, text="0", width=3).grid(row=4,column=1)
bponto = tkinter.Button(num, text=".", width=3).grid(row=4,column=2)
bdiv = tkinter.Button(num, text="/", width=3).grid(row=4,column=3)

bresul = tkinter.Button(window, text="=", width=7)
bresul.pack()

esp4 = tkinter.Label(window, text="")
esp4.pack()

quitb = tkinter.Button(window, text="Quit", command=sair)
quitb.pack()

window.mainloop()
