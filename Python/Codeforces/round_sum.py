if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        l = ""
        count = 0

        if n in [1,2,3,4,5,6,7,8,9]:
            print(1)
            print(n)

        else:
            if(n%1000 == 0 and n%100 == 0 and n%10 == 0):
                count = count + 1
                print(count)
                print(n)
            else:
                if(n%10 != 0):
                    n1 = n%10
                    l = l + str(n1) + " "
                    n = n - n1
                    count = count + 1

                if(n > 100):
                    if(n%100 != 0):
                        n2 = n%100
                        l = l + str(n2) + " "
                        n = n - n2
                        count = count + 1

                if(n > 1000):
                    if(n%1000 != 0):
                        n3 = n%1000
                        l = l + str(n3) + " "
                        n = n - n3
                        count = count + 1
                
                l = l + str(n)
                print(count+1)
                print(l)
