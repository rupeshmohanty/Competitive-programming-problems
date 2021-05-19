if __name__ == "__main__":
    n = int(input())
    card = list(map(int,input().split()))
    (s,d) = (0,0)

    if(n <= 4):
        for i in range(0,int(n/2)):
            d = d + card[i]
        
        for i in range(int(n/2),n):
            s = s + card[i]
    else:
        if(n % 2 == 0):
            for i in range(n):
                if(i % 2 == 0):
                    s = s + card[i]
                else:
                    d = d + card[i]
        else:
            for i in range(1,n):
                if(i % 2 == 0):
                    s = s + card[i]
                else:
                    d = d + card[i]
            s = s + card[0]

    print(s,d)