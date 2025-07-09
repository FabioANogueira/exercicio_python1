from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM


root = Tk() # instancia uma janela
photo = PhotoImage(file='imagegif.gif').subsample(3) #insere imagem
image = Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=("Courier", 18), text='Olá Alunos da Univesp')
text.pack(side=BOTTOM)



#hello = Label(master=root, text='Olá Mundo', image=photo, width=300, height=180) #atributos
#hello.pack() # empacotamento

root.mainloop() #mostrar janela na tela




