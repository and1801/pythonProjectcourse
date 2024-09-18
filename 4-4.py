my_dict = {
    'name': 'имя',
    'car': 'машина',
    'apple': 'яблоко',
    'book': 'книга'
}

print(my_dict.get('car'))
print(my_dict.items())
print(my_dict.values())
print(my_dict.keys())
a = my_dict.pop('name')
print(a)
b = my_dict.popitem()
print(b)
my_dict.update({'book': 'чтиво' , 'cat': 'кот'})
print(my_dict)
