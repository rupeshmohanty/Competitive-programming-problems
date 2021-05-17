if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        res = []

        for i in range(2*n):
            if(arr[i] not in res):
                res.append(arr[i])
        
        r = " ".join(str(e) for e in res)
        print(r)