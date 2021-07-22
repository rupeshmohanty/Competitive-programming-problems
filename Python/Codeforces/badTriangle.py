if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        res = [1,2]
        count = 0

        for i in range(n):
            if(arr[0] + arr[1] <= arr[i]):
                res.append(i+1)
                count = 1
                break
            else:
                continue
        if(count == 0):
            print(-1)
        else:
            print(" ".join(str(e) for e in res))