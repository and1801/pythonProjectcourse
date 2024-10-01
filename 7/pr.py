try:
    number = int(input('enter a number: '))
    print(number)
except:
    print('преобразование не произошло')
else:
    print('try 0 errors')
finally:
    print('выполняется в любом случае')
print('end')