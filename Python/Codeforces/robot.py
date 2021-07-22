if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        x,y = map(int,input().split())
       
        if(x == y):
            print(x+y)
        else:
            print(2*max(x,y) - 1)