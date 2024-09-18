from audioop import reverse

a = []
a.append(2)
a.append(5)
a.append(7)

a.insert(0, 9)
a.insert(1, 10)
a.sort()
a.reverse()
print(a)
