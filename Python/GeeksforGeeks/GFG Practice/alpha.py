n = int(input())
s = list(map(str,input().split()))
res = []

for i in s:
    if i.isdigit():
        res.append(i)

m = 0
for i in res:
    if '9' not in i:
        if int(i) > m:
            m = int(i)

print(m)