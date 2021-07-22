if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        res = []

        for i in range(n):
            res.append(arr.count(arr[i]))

        print(max(res))
