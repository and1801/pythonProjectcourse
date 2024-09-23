def sum_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total


sum = sum_range(1, 5)
print(sum)