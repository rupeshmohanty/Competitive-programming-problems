if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        m = pow(2,n)
        b = input()
        (c,d) = (0,0)

        for i in range(m):
            a = bin(i).replace('0b','')
            if(a[0] == '1'):
                temp = int(a) + int(b)

                if(temp > c):
                    a = bin(i).replace('0b','')
                    break
        
        print(a)
        

        
