from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime


def clicked():
    global entry
    date = entry.get()
    weekday = strftime ('%A', strptime(date, '%b %d, %Y '))
    showinfo(message='{} was um {}'.format(date, weekday))
    showinfo(message=time)


root = Tk() # cria a janela
label = Label(root, text='Digite uma data: ')
label.grid (row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
button = Button(root, text='Clique aqui',command=clicked) # cria o botão
button.grid(row=1, column=0, columnspan=2) 
root.mainloop() #chama a janela
