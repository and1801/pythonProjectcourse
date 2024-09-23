def bank(a, years):
    for n in range(1, years + 1):
        S = a*((1 + (10/100)) **n)
    return S

Sumvkl = bank(1000, 3)
print(Sumvkl)