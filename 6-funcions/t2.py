def square(lengh):
    P = lengh * 4
    S = lengh **2
    d = lengh * (2 ** (1 / 2))
    return P, S, d

num1, num2, num3 = square(5)
print(num3, num2, num1)