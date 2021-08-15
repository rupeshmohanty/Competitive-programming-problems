d = {}
words = list(map(str,input().split()))

for i in words:
    x = "".join(sorted(list(i)))
    if x in d:
        d[x].append(i)
    else:
        d[x] = [i]

print(sorted(d.values()))
    