def sum(a,b):
    try:
        result = a + b
    except TypeError:
        return "Ошибка: неверный тип данных. Оба аргумента должны быть числами."
    else:
        return result

def multip(a, b):
    try:
        result = a * b
    except TypeError:
        return "Ошибка: неверный тип данных. Оба аргумента должны быть числами."
    else:
        return result

def div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль."
    except TypeError:
        return "Ошибка: неверный тип данных. Оба аргумента должны быть числами."
    else:
        return result


def sub(a,b):
    try:
        result = a - b
    except TypeError:
        return "Ошибка: неверный тип данных. Оба аргумента должны быть числами."
    else:
        return result
