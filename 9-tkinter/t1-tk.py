import tkinter as tk

def say_hello():
    name = entry.get()
    greeting = f'Привет, {name}'
    greeting_label.config(text=greeting)

root = tk.Tk()
root.title('Hi!')

label = tk.Label(root, text= 'Введите имя: ')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='Поздороваться', command= say_hello)
button.pack()

greeting_label = tk.Label(root, text='')
greeting_label.pack()


root.mainloop()