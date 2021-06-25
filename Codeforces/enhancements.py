if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        res = set()
        
        for i in arr:
            if i in res:
                res.add(i+1)
            else:
                res.add(i)
        
        print(len(res))
