for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    j = 0
    k = n - 1

    rsum,lsum = 0,0

    # mid index!
    mid = n // 2
    # Finding right sum!
    for k in range(n):
        rsum += arr[k]
    
    j = 0
    res = 0
    flag = False
    # checking the sum on the left hand side!
    while j < n:
        rsum -= arr[j]

        if lsum == rsum:
            flag = True
            res = j
            break 
        lsum += arr[j]
        j += 1 
    
    if flag:
        print(res)
    else:
        print(-1)