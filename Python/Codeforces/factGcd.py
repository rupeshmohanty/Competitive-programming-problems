if __name__ == "__main__":
    a,b = map(int,input().split())
    x = 1
    n = min(a,b)

    for i in range(1,n+1):
        x *= i

    print(x)