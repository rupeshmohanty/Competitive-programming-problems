if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        a,b,c,d = map(int,input().split())
        (x,y,z) = (0,0,0)

        for i in range(1,d+1):
            if(i >= a and i <= b):
                x = i
            
            if(i >= b and i <= c):
                y = i
            
            if(i >= c and i <= d):
                z = i

            if(x != 0 and y != 0 and z != 0):
                if(x + y > z):
                    break
                else:
                    continue
        
        print(x,y,z)