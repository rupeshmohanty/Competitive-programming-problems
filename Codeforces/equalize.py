if __name__ == "__main__":
    q = int(input())

    for _ in range(q):
        n = int(input())
        arr = list(map(int,input().split()))
        s = 0

        s = sum(arr)

        if(s % n == 0):
            print(int(s/n))
        else:
            print(int(s/n) + 1)