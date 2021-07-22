if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        minm = abs(arr[1] - arr[0])

        for i in range(n):
            for j in range(n):
                if(i != j):
                    minm = min(abs(arr[i] - arr[j]),minm)
        
        print(minm)