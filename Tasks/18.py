s = 'abcdeabc'
cleaned_string = ''.join(sorted(set(s), key=s.index))
print("Строка без дублей символов:", cleaned_string)
