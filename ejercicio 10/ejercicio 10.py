import tkinter
from tkinter import ttk
window = tkinter.Tk()

def choice(n):
    print(f"se ah seleccioado la opcion Nº:{n}")
    

def resetFunc(evt):
    selectedOp.set(None)


selectedOp = tkinter.StringVar()

RB1 = ttk.Radiobutton(window,text="opcion1",value="1", variable=selectedOp)
RB2 = ttk.Radiobutton(window,text="opcion2",value="2", variable=selectedOp)
RB3 = ttk.Radiobutton(window,text="opcion3",value="3", variable=selectedOp)
reset = tkinter.Button(window,text="reiniciar")

RB1.bind("<Button-1>",lambda x:choice(1))
RB2.bind("<Button-1>",lambda x:choice(2))
RB3.bind("<Button-1>",lambda x:choice(3))
reset.bind("<Button-1>",resetFunc)
RB1.pack()
RB2.pack()
RB3.pack()
reset.pack()

window.mainloop()
