if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n,m = map(int,input().split())
        arr = list(map(int,input().split()))
        s = sum(arr)

        if(s == m):
            print("YES")
        else:
            print("NO")