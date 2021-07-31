n,k = map(int,input().split())
arr = list(map(int, input().split()))
res = []
temp = []

for i in range(len(arr)):
    res.append(arr[i] % k)

print(res)
for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j:
            if res[i] + res[j] == k:
                if res.count(res[i]) > res.count(res[j]):
                    if res[i] not in temp:
                        temp.append(res[i])
                elif res.count(res[i]) < res.count(res[j]):
                    if res[j] not in temp:
                        temp.append(res[j])
                else:
                    if res[i] not in temp:
                        temp.append(res[i]) 

print(len(temp))
