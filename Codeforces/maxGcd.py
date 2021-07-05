def gcd(a,b):
    maxm = 0
    for i in range(2,max(a,b)):
        if a % i == 0 and b % i == 0:
            if i > maxm:
                maxm = i
    if maxm == 0:
        return 1
    else:
        return maxm

if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        res = []

        for i in range(1,n+1):
            for j in range(1,n+1):
                r = gcd(i, j)
                res.append(r)
        
        print(max(res))