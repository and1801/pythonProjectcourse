def pluralize(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word.endswith('s') or word.endswith('x') or word.endswith('z') or word.endswith('ch') or word.endswith('sh'):
        return word + 'es'
    else:
        return word + 's'

noun = input("Введите существительное в единственном числе: ")
plural_noun = pluralize(noun)
print("Множественное число:", plural_noun)
