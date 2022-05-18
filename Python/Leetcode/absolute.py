arr = list(map(int,input().split()))
arr.sort()
res = []
m = abs(arr[1] - arr[0])

for i in range(len(arr)-1):
    if abs(arr[i+1] - arr[i]) < m:
        m = abs(arr[i+1] - arr[i])

for i in range(len(arr)-1):
    if abs(arr[i+1] - arr[i]) == m and [arr[i],arr[i+1]] not in res:
        res.append([arr[i],arr[i+1]])

print(res)