if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n, m = map(int,input().split())
        prod = n*m

        temp = int(prod/2)

        print(prod-temp)