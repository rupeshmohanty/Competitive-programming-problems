if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        a, b = map(int,input().split())
        count = 0
        temp = 0

        if(a == b):
            print(count)
        else:
            sum = 0
            if(a > b):
                temp = a - b
                if(temp % 2 == 0):
                    count = count + 1
                else:
                    count = 2
            else:
                temp = b - a
                if(temp % 2 != 0):
                    count = count + 1
                else:
                    count = 2

            print(count)
                    
                        