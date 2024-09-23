def f():
    global text 

    text = 'глобальная переменная'
    print(f'внутри - {text}')

f()
print(text)