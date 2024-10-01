import random
import tkinter


students_list = [
    "Kim", "Chan", "In", "Huilo", "PbIHR", "Sdoh", "Ni", "MPA3b"
]

print(dir(tkinter))
random_students = random.sample(students_list, 5)

print('Имена  отвечающих учащихся: ')
for i in random_students:
    print(i)