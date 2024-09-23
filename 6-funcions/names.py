def hello(*names):
    print(names)
    for name in names:
        print('hello', name)
hello('Alice', 'Bob', 'Carl')