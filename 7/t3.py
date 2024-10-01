def bank():
    try:
        a = float(input('Введите сумму вклада: '))
        years = int(input('Введите количество лет вклада: '))
        for n in range(1, years + 1):
            S = a*((1 + (10/100)) **n)
        return S

    except:
        print('Введите корректные значения')

print(bank())