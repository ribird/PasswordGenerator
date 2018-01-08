#!/usr/bin/python3

import sys, random, tkinter
from tkinter import *

def generate():
    text.delete('1.0', END)
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*^"
    pw = ""
    for i in range(0,12):
        pw += chars[random.randint(0, len(chars) - 1)]
    text.insert(END, pw)
        
top = Tk()
top.title('Password Generator')
top.geometry('%dx%d+%d+%d' % (150, 50, 1150, 50))
text = Text(top, height=1, width=12)
text.pack()
b = tkinter.Button(top, text = "Generate", command = generate)
b.pack()
top.resizable(0,0)
mainloop()
