import tkinter as tk
from cProfile import label

root = tk.Tk()

root.title('Первый проект')

label = tk.Label(root, text = 'это первый текст в нашем приложении')
label.pack()

def on_button_click():
    label.config(text='кнопка была нажата')


button = tk.Button(root, text ='нажми на меня', command=on_button_click)

button.pack()

root.mainloop()