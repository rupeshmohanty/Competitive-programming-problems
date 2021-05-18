if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        a,b,c,n = map(int,input().split())
        temp = max(a,b,c)
        reqd = (temp-a) + (temp-b) + (temp-c)
        if(reqd > n):
            print("NO")
        else:
            n = n - reqd

            if(n % 3 == 0):
                print("YES")
            else:
                print("NO")
