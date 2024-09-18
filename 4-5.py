set1 = {1, 2, 5, 5, 4, 6, 7}
set2 = {3, 8, 5, 6, 7, 9, 10}
print(set1)
set1.add(9)
print(set1)
set1.remove(5)
print(set1)
set_unio = set1.union(set2)
print(set_unio)
set_dif = set1.difference(set2)
print(set_dif)
