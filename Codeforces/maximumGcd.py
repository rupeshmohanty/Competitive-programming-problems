if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        temp = 0

        for i in range(1,n+1):
            for j in range(i,n+1):
                if(i != j):
                    if(j % i == 0):
                        if(min(i,j) > temp):
                            temp = min(i,j)
                    else:
                        if(j%i > temp):
                            temp = j%i

        print(temp) 