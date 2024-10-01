import tkinter as tk
from cProfile import label
from tkinter import Button

root = tk.Tk()

button1 = Button(root, text='Кнопка 1')
button2 = Button(root, text='кнопка 2')
button1.grid(row=0, column=1)
button2.place(x =50,y = 200)
root.mainloop()