from tkinter import Tk, Text, BOTH

def key_pressed(event):
    print('char: {}'.format(event.keysym))