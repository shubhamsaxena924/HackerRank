n = int(input())
a = input()
l = []
b = a.split()
for i in b:
    l.append(int(i))
c = sorted(list(set(l)))
print(c[len(c)-2])
