if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        a,b,n = map(int,input().split())
        res = 0

        for k in range(n):
            if(a > b):
                b += a
                res += 1
            else:
                a += b
                res += 1
            
            if(a > n or b > n):
                break
        
        print(res)
