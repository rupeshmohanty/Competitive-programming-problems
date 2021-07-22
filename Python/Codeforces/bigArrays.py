if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        minm = min(arr)

        if(arr.count(minm) == n):
            print(0)
        else:
            print(n - arr.count(minm))
        

        
