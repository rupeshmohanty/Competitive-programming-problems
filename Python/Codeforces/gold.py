t = int(input())

for _ in range(t):
    n,x = map(int, input().split())
    arr = list(map(int, input().split()))
    s = 0
    res = []

    if sum(arr) == x:
        print("NO")
    else:
        for i in range(n):
            if s + arr[i] != x:
                s += arr[i]
                res.append(arr[i])
        
        for j in range(n):
            if arr[j] not in res:
                res.append(arr[j])

        if s == 0:
            print("NO")
        else:
            print("YES")
            print(" ".join(str(e) for e in res))
