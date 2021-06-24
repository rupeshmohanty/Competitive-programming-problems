if __name__ == "__main__":
    n,m = map(int,input().split())
    count = 0

    for i in range(0,max(n,m)+1):
        for j in range(0,max(n,m)+1):
            (exp1,exp2) = (0,0)
            
            exp1 = pow(i,2) + j
            exp2 = i + pow(j,2)

            if(exp1 == n and exp2 == m):
                count += 1
        
    print(count)