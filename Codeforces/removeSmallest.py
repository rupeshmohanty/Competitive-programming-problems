t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    res = []

    for i in range(1,n):
        if(abs(arr[i] - arr[i-1]) <= 1):
            res.append(min(arr[i],arr[i-1]))
        
    if n - len(res) == 1:
        print("YES")
    else:
        print("NO")