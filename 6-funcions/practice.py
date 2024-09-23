def season(month):
    if 1 <= month <= 12:
        if month == 12 or month == 1 or month == 2:
            return 'зима'
        elif month == 3 or month == 4 or month == 5:
            return 'весна'
        elif month == 6 or month == 7 or month == 8:
            return 'лето'
        elif month == 9 or month == 10 or month == 11:
            return 'осень'
    else:
        print('нет такого месяца')

season_month = season(9)
print(season_month)