if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        x,y,n = map(int,input().split())
        temp = int(n/x)
        sum = 0

        if(n % x == y):
            print(n)
        else:
            for i in range(n):
                sum = sum + x*temp + y
                if(sum < n):
                    break
                else:
                    temp = temp - 1
                    sum = 0
            
            print(sum)