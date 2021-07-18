n = int(input())
maxm = 0
res = []
d = dict()

for _ in range(n):
    name = input()
    marks = float(input())

    d[name] = marks

l = list(d.values())
l.sort()

for i in reversed(list(d.keys())):
    if d[i] == l[1]:
        print(i)
