if __name__ == "__main__":
    n, k = map(int,input().split())
    sum = k
    count = 0

    for i in range(1,n+1):
        sum = sum + 5*i
        if(sum <= 240):
            count = count + 1
    
    print(count)