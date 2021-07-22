if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        res = []

        for i in range(n):
            if(arr.count(arr[i]) == 1):
                res.append((arr[i],i+1))
            else:
                continue
        
        if(len(res) == 0):
            print(-1)
        else:
            print(min(res)[1])
