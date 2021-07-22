if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        win = 0

        if(arr.count(arr[0]) == n):
            print(0)
        else:
            m = min(arr)
            win = n - arr.count(m)
            print(win)
                