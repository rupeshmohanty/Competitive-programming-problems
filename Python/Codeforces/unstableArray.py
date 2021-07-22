if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n, m = map(int,input().split())

        if(n == 1):
            print(0)
        elif(n == 2):
            print(m)
        else:
            print(min(2,n-1)*m)