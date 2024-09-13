def time_converter(seconds):
    days = seconds // 86400  # Секунды в днях
    seconds %= 86400
    hours = seconds // 3600  # Секунды в часах
    seconds %= 3600
    minutes = seconds // 60  # Секунды в минутах
    seconds %= 60

    return f"{days}д:{hours}ч:{minutes}м:{seconds}с"


# Пример использования
total_seconds = int(input("Введите количество секунд: "))
converted_time = time_converter(total_seconds)
print(f"Конвертированное время: {converted_time}")
