if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        a, b = map(int,input().split())
        res = 0
        
        if(a == b):
            print(0)
        else:
            res = abs(a-b)
            if(res % 10 == 0):
                res = res/10
                print(int(res))
            else:
                res = res/10
                print(int(res+1))
        
        