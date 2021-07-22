if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        arr.sort()
        (temp,count) = (0,0)

        for i in range(2*n - 1):
            if arr[i] % 2 == 0:
                if arr[i+1] % 2 != 0:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
            
        print(" ".join(str(e) for e in arr))