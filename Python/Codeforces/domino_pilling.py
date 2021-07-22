if __name__ == "__main__":
    M, N = map(int, input().split())
    count = 0
    sum = 0
    
    for i in range(M*N):
        sum = sum + 2
        if(sum <= M*N):
            count = count + 1
    
    print(count)