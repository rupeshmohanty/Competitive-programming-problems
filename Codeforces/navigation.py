if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        x,y = map(int,input().split())
        s = input()
        (count1,count2) = (0,0)
        (u,d,r,l) = (0,0,0,0)
        
        u = s.count('U')
        d = s.count('D')
        r = s.count('R')
        l = s.count('L')


        if(x > 0):
            if(r >= x):
                count1 += 1
        else:
            if(-l <= x):
                count1 += 1
        
        if(y > 0):
            if(u >= y):
                count2 += 1
        else:
            if(-d <= y):
                count2 += 1
        
        if(count1 > 0 and count2 > 0):
            print("YES")
        else:
            print("NO")
