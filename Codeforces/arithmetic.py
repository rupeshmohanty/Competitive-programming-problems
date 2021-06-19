if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = map(int,input().split())
        s = sum(arr)

        if(s == n):
            print(0)
        elif(s > n):
            print(s-n)
        else:
            print(1)
                