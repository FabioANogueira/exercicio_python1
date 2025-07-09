from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo
from time import strftime, localtime


def clicked():
    time = strftime('Day: %d %b %y \n Time: %H:%M:%S %p \n', localtime())
    showinfo(message=time)



root = Tk() # cria a janela
button = Button(root, text='Clique aqui',command=clicked) # cria o botão
button.pack() #empacota a janela
root.mainloop() #chama a janela
