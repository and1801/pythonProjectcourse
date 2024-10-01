try:
    a = int(input())
    b = int(input())
    c = a/b
except ValueError:
    print('neto')
except ZeroDivisionError:
    print('0')

print('end')