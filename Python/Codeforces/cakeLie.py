if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n,m,k = map(int,input().split())
        (x,y) = (1,1)
        (a,b) = (0,0)

        if(n != x or m != y):
            
            while(x < n or y < m):
                if(y != m):
                    y += 1
                    a += x
                if(x != n):
                    x += 1
                    b += y
        
        if(a + b == k):
            print("YES")
        else:
            print("NO")
        