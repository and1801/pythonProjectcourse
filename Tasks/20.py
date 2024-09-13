text = "apple ant bat apple antelope arm"
words = text.split()
words_starting_with_a = [word for word in words if word.startswith('a')]
print("Слова, начинающиеся на 'a':", words_starting_with_a)
