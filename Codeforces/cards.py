if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        w,h,n = map(int,input().split())
        count = 0
        product = w*h

        if(product % 2 == 0):
            while(product % 2 == 0):
                count = count + 2
                product = int(product/2)
        else:
            count = 1

        print(count)

        if(count >= n):
            print("YES")
        else:
            print("NO")
        
