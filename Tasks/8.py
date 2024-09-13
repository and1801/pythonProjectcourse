def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Пример использования
num = int(input("Введите число от 0 до 1000: "))
if 0 <= num <= 1000:
    if is_prime(num):
        print(f"{num} - это простое число.")
    else:
        print(f"{num} - это не простое число.")
else:
    print("Число должно быть в диапазоне от 0 до 1000.")