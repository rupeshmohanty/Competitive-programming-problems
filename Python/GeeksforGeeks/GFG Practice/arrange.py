n = int(input())
arr = list(map(int,input().split()))
res = []

for i in range(n):
    res.append(arr[arr[i]])

for i in range(n):
    arr.pop()

arr += res
print(" ".join(str(e) for e in arr))