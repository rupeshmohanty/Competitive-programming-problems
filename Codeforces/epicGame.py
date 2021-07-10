def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x % y)

if __name__ == "__main__":
    a,b,n = map(int, input().split())

    i = 0
    while(n >= 0):
        if i % 2 == 0:
            n -= gcd(max(a, n),min(a, n))
        else:
            n -= gcd(max(b,n), min(b, n))
        i += 1
    
    print(i % 2)