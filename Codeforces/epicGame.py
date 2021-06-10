def gcd(x,y):
    g = 0

    if(y < x):
        return 0
    else:
        for i in range(1,y):
            if(x % i == 0 and y % i == 0):
                g = i
        return g

if __name__ == "__main__":
    a,b,n = map(int,input().split())
    i = 0
    (s,an) = (0,0)

    while(n >= 0):
        if(i % 2 == 0):
            if(gcd(a,n) != 0):
                n = n - gcd(a,n)
            else:
                s += 1
                break
        else:
            if(gcd(b,n) != 0):
                n = n - gcd(b,n)
            else:
                an += 1
                break

        i += 1

    if(s == 1):
        print(0)
    else:
        print(1)
    

