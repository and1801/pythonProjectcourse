def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Пример использования
year = int(input("Введите год: "))
if is_year_leap(year):
    print(f"{year} год является високосным.")
else:
    print(f"{year} год не является високосным.")
