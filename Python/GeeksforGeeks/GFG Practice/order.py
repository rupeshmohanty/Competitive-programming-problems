n = int(input())
arr = list(map(int,input().split()))
res = []

for i in range(n):
    if arr[i] % 10 != 0:
        res.append(arr[i])

for i in range(n):
    if arr[i] not in res:
        res.append(arr[i])

print(res)