if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        res = []

        for i in range(1,n+1):
            for j in range(i,n+1):
                if(i != j):
                    if(j % i == 0):
                        res.append(min(i,j))
                    else:
                        res.append(j%i)
        
        print(max(res))