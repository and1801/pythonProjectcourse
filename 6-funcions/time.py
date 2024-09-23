from datetime import datetime

def print_current_time():
    # Получаем текущее время
    current_time = datetime.now().time()
    # Выводим текущее время в формате ЧЧ:ММ:СС
    print("Текущее время:", current_time.strftime("%H:%M:%S"))

# Вызов функции
print_current_time()