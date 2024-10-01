import tkinter as tk

def say_hell0():
    name = entry.get()
    greeting_label.config(text=f'Hello {name}')

root = tk.Tk()

root.title('say hell0')

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text='подтвердить ввод', command=say_hell0)
submit_button.pack()

greeting_label = tk.Label(root, text ='здесь будет приветствие')
greeting_label.pack()

root.mainloop()



