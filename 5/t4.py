start = int(input('начало диапазона '))
end = int(input('конец диапазона '))
print("Четные числа в диапазоне от", start, "до", end, ":")
for i in range(start, end + 1):
    if i %2 == 0:
        print(i)