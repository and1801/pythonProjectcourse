import random

text = "This is a sample text with several words"
words = text.split()
random.shuffle(words)
shuffled_text = ' '.join(words)
print("Перемешанный текст:", shuffled_text)
