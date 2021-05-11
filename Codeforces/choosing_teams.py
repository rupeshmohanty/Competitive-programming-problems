if __name__ == "__main__":
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    res = []
    (sum,count) = (0,0)

    for i in range(n):
        if(abs(n-k) == 1):
            if(arr[i] <= abs(n-k)):
                res.append(arr[i])
        else:
            if(arr[i] < abs(n-k)):
                res.append(arr[i])
    
    for k in range(len(res)):
        if(len(res) < 3):
            count = 0
        else:
            count = int(len(res)/3)

    print(count)