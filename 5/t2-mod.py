user_input = input('введите операцию - ')
num1, operator, num2 = user_input.split()
num1 = float(num1)
num2 = float(num2)

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 + num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/' and num2 != 0:
    result = num1 / num2
    print(result)