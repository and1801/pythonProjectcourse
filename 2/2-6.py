def caesar_cipher(text, shift, mode='encrypt'):
    result = ''

    # Если режим дешифрования, сдвиг должен быть отрицательным
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            # Определяем базу (большая или маленькая буква)
            start = ord('A') if char.isupper() else ord('a')
            # Шифруем или дешифруем символ и добавляем его к результату
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Если символ не буква, оставляем его без изменений
            result += char

    return result


# Пример использования
text = "Hello, World!"  # Текст для шифрования/дешифрования
shift = 6  # Сдвиг для шифра

# Шифрование
encrypted_text = caesar_cipher(text, shift, mode='encrypt')
print(f"Зашифрованный текст: {encrypted_text}")

# Дешифрование
decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
print(f"Расшифрованный текст: {decrypted_text}")
