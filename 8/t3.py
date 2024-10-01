import random

def select_students(students, num_to_select = 5):
    if num_to_select > len(students):
        raise ValueError("Количество студентов для выбора больше, чем доступно в списке")

    select_students = random.sample(students, num_to_select)
    return select_students

students_list = [
    "Kim", "Chan", "In", "Huilo", "PbIHR", "Sdoh", "Ni", "MPA3b"
]

select_students = select_students(students_list, 2)

print("студенты, которые ответят: ")
for student in select_students:
    print(student)

print (random.sample(students_list, 5))