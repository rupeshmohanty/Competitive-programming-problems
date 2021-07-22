t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    res = []
    temp = []
    arr.sort()

    for i in range(n):
        if arr[i] not in res:
            res.append(arr[i])
        else:
            temp.append(arr[i])
        
    res.extend(temp)
    print(" ".join(str(e) for e in res))

    