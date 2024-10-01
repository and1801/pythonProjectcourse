while True:
    try:
      a = int(input("Введите число: "))
      break
    except ValueError:
      print("Ошибка: Пожалуйста, введите числовые значения.")
    except TypeError:
      print('Неподходящий тип')
