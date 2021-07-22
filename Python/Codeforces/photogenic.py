if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        res = []
        temp = 0

        for i in range(n):
            if(arr[i] % 2 == 0):
                res.append(arr[i])
                
        for i in range(n):
            if(arr[i] % 2 != 0):
                res.append(arr[i])
        
        print(" ".join(str(e) for e in res))
