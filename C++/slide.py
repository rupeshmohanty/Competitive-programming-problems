n = int(input())
arr = list(map(int,input().split()))
k = int(input())
res = []

for i in range(k,n):
    res.append(arr[i])

for i in range(k):
    res.append(arr[i])

print(res)