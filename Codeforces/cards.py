if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        w,h,n = map(int,input().split())
        count = 1
        product = w*h

        if product % 2 == 0:
            while(product % 2 == 0):
                product = int(product/2)
                count *= 2
            
            if count >= n:
                print("YES")
            else:
                print("NO")
        else:
            if n == 1:
                print("YES")
            else:
                print("NO")
        
