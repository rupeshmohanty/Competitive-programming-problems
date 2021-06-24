if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))

        s = arr[::-1]
        print(" ".join(str(e) for e in s))