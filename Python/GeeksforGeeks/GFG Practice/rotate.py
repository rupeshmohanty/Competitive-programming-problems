n = int(input())
arr = list(map(int,input().split()))
k = int(input())
res = []
c = 0

for i in range(n-1,-1,-1):
    res.append(arr[i])
    c += 1
    if c == k:
        break

res.sort()

for j in range(n):
    if arr[j] not in res:
        res.append(arr[j])

print(" ".join(str(e) for e in res))