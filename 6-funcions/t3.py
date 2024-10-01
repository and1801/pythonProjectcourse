def bank(a, years):
    for n in range(1, years + 1):
        S = a*((1 + (10/100)) **n)
        print(f'вклад итого: {S}')
    return S

res = bank(5000, 2)
print(f'всего - {res}')


