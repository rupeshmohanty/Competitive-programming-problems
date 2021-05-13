if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        maxm = pow(2,n)
        minm = 0

        for j in range(1,int(n/2)):
            maxm = maxm + pow(2,j)
        
        for k in range(int(n/2),n):
            minm = minm + pow(2,k)

        print(abs(maxm - minm))

