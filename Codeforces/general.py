if __name__ == "__main__":
    n = int(input())
    l = list(map(int,input().split()))
    temp = 0
    count = 0

    for i in range(len(l)):
        if(l[0] < l[i]):
            # swapping
            temp = l[0]
            l[0] = l[i]
            l[i] = temp
            count = count + 1
        elif(l[n-1] > l[i]):
            # swapping
            temp = l[n-1]
            l[n-1] = l[i]
            l[i] = temp
            count = count + 1
        else:
            continue
        
        print(l)
        
    print(count)