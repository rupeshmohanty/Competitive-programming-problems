if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        c = list(map(int,input().split()))
        s = " ".join(str(e) for e in c)

        c1 = s.count('1')
        c2 = s.count('2')
        sum = 0

        sum = c1*1 + c2*2

        if(n % 2 == 0):
            if(sum % 2 == 0):
                print("YES")
            else:
                print("NO")

        else:
            if(c1 == 0 or c2 == 0):
                print("NO")
            else:
                if(sum % 2 == 0):
                    print("YES")
                else:
                    print("NO")
        
        