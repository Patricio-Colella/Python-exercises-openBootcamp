import tkinter
from tkinter import ttk
import pprint



window = tkinter.Tk()

listEn = ["red","blue","yellow","green"]
listEs = ["rojo","azul","amarrillo","verde"]
color = "white"
listEs = tkinter.StringVar(value=listEs)

def changeColor(evt):
    
    color=(listEn[listToRender.curselection()[0]])
    global coloredLabel
    coloredLabel["bg"]=color
    

listToRender = tkinter.Listbox(window,listvariable=listEs)
toogle = tkinter.Button(window,text="cambiar color")
coloredLabel = tkinter.Label(window,text="¡COLOREAME!",bg=color)

toogle.bind("<Button-1>",changeColor)
listToRender.pack()
toogle.pack()
coloredLabel.pack()

window.mainloop()
