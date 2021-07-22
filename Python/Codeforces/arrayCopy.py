if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))

        s = set(arr)

        print(len(s))