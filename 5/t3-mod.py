month = int(input('номер месяца - '))
month_day = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}
if 1 <= month <=12:
    print(f'Количество дней в месяце - {month_day[month]}')
else:
    print('неверный номер месяца')