if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        k = int(input())
        
        if(100 % k == 0):
            print(int(100/k))
        else:
            max = 0

            for i in range(2,100):
                if(100 % i == 0 and k % i == 0):
                    if(i > max):
                        max = i
                
            if(max != 0):
                print(int(100/max))
            else:
                print(100)