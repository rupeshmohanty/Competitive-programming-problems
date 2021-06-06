if __name__ == "__main__":
    t = int(input())

    for test in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        res = []
        (pos1,pos2) = (0,0)
        count = 0

        for i in range(n):
            if(arr[i] == 1):
                res.append(i)
            else:
                continue
        
        pos1 = min(res)
        pos2 = max(res)

        for j in range(pos1,pos2+1):
            if(arr[j] == 0):
                count += 1
        
        print(count)