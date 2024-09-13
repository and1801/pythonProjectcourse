nested_list = [
    [],
    [],
    [
        [11, 12, 13],
        [14, 15, 16],
        [17, 17, 19],
        [21, 22, 23],
        [24, 25, 26],
        [27, 27, 29],
        [31, 32, 33],
        [34, 35, 36],
        [37, 37, 39]
    ]
]
total_sum = sum(sum(inner_list) for inner_list in nested_list[2])
print("Сумма элементов списка:", total_sum)
