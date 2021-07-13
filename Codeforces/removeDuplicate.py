n = int(input())
arr = list(map(int, input().split()))
res = []

for i in range(n-1,-1,-1):
    if arr[i] not in res:
        res.append(arr[i])

print(len(res))
print(" ".join(str(e) for e in res[::-1]))