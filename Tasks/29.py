def prime_factors(n):
    factors = []
    # Считаем количество раз, которое 2 делит n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Теперь n должно быть нечетным. Проверяем нечетные числа.
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

number = int(input("Введите целое число: "))
factors = prime_factors(number)
print("Простые множители числа:", factors)
