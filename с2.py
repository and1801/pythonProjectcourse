def is_palindrome(s):
    # Приводим строку к нижнему регистру и убираем все пробелы и знаки препинания
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Проверяем, равна ли строка своей перевёрнутой версии
    return s == s[::-1]


# Пример использования
text = "A man, a plan, a canal, Panama"
if is_palindrome(text):
    print(f'"{text}" является палиндромом.')
else:
    print(f'"{text}" не является палиндромом.')