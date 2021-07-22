n = int(input())
arr = list(map(int, input().split()))
p = int(input())
res = []

for i in range(1,n+1):
    res.append(arr.count(i))

print(" ".join(str(e) for e in res))