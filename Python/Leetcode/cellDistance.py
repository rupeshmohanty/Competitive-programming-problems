rows,cols = map(int,input().split())
rCenter, cCenter = map(int,input().split())
res = []
d = []

for i in range(rows):
    for j in range(cols):
        d.append([abs(i - rCenter) + abs(j - cCenter),[i,j]])

d.sort(key=lambda x:x[0])

for i in range(len(d)):
    res.append(d[i][1])

print(res)