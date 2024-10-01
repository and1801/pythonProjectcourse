import tkinter as tk

def my_sum():
    numbers = entry.get().split()
    result = 0
    for number in numbers:
        number = int(number)
        result += number
    label.config(text=f'сумма чисел - {result}')


root = tk.Tk()
root.title('Сумма чисел: ')

label = tk.Label(root, text= 'введите числа через пробел')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='посчитать сумму', command=my_sum)
button.pack()

root.mainloop()