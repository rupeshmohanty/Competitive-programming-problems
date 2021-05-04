if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    (max,min) = (a[0],a[0])
    count = 0

    for i in range(n):
        if(a[i] > max):
            max = a[i]
            count = count + 1
        elif(a[i] < min):
            min = a[i]
            count = count + 1
        else:
            continue
    
    print(count)