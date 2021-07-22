if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        # declare variables!
        n, k = map(int,input().split())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        sumA = 0
        sumB = 0

        a.sort()
        b.sort()

        for i in range(n):
            sumA = sumA + a[i]
            sumB = sumB + b[i]

        if(sumA < sumB):
            sumA = 0
            for i in range(k):
                a[i],b[n-i-1] = b[n-i-1],a[i]
            
            for i in range(n):
                sumA = sumA + a[i]

        print(sumA)