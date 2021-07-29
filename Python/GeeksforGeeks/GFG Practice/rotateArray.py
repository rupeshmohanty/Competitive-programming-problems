for i in range(int(input())):
    n,d = map(int, input().split())
    arr = list(map(int,input().split()))
    res = []

    for i in range(d,n):
        res.append(arr[i])
    
    for j in range(d):
        res.append(arr[j])

    print(" ".join(str(e) for e in res))