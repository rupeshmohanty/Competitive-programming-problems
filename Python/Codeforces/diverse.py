n,k = map(int, input().split())
arr = list(map(int, input().split()))
res = []
pos = []

for i in range(n):
    if len(res) == k:
        break
    else:
        if arr[i] not in res:
            res.append(arr[i])
            pos.append(i+1)

if len(res) == k:
    print("YES")
    print(" ".join(str(e) for e in pos))
else:
    print("NO")