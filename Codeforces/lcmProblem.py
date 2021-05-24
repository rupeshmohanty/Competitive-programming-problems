if __name__ == "__main__":
    t = int(input())

    while(t > 0):
        l, r = map(int,input().split())

        if(2*l > r):
            print(-1,-1)
        else:
            print(l,2*l)

        t -= 1