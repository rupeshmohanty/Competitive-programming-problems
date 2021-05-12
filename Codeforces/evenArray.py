if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        e = []
        o = []

        for i in range(n):
            if(i % 2 == 0):
                if(a[i] % 2 != 0):
                    e.append(a[i])
            else:
                if(a[i] % 2 == 0):
                    o.append(a[i])
        
        if(len(e) != len(o)):
            print(-1)
        else:
            print(len(o))