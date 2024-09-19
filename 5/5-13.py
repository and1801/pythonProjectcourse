num = int(input('enter a number: '))
while num !=0:
    if num < 0:
        print('negative')
        break
    num = int(input('enter a number: '))
else:
    print('no negative')