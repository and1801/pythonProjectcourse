
my_list = [1, 2, 3, 5, 4]
try:
    index = int(input('введите индекс элемента: '))
    print(my_list[index])
except:
    print('такого элемента нет')