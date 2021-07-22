if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        count = 0
        p = 0

        if(n % 2050 != 0):
            print(-1)
        else:
            p = int(n/2050)

            if(p < 10):
                print(p)
            else:
                temp = 0
                while(p != 0):
                    temp = p % 10
                    count += temp
                    p = int(p/10)
                
                print(count)
