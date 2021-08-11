n = int(input())
arr = list(map(int,input().split()))
k = int(input())
res = []

for i in range(n-k,n):
    res.append(arr[i])

for i in range(0,n-k):
    res.append(arr[i])

print(" ".join(str(e) for e in res))