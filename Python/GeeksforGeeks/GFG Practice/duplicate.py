n = int(input())
a = list(map(int, input().split()))
res = []

for i in a:
    if a.count(i) > 1:
        if i not in res:
            res.append(i)

if len(res) > 0:
    for i in res:
        print(i)
else:
    print(-1)