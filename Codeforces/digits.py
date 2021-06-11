if __name__ == "__main__":
    k2,k3,k5,k6 = map(int,input().split())
    (a,b,s) = (0,0,0)

    a = min(k2,k5,k6)
    k2 = k2 - a
    b = min(k2,k3)

    s = 256*a + 32*b
    print(s)
