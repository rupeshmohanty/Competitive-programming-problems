if __name__ == "__main__":
    n = int(input())
    l = []
    count = 0

    # appending the values to the list!
    for i in range(n):
        temp = int(input())
        l.append(temp)

    # for one element, there is only one group!
    if(n == 1):
        count = 1
        print(count)
        exit()

    # for two elements, there is only one group for same elements but two groups for different elements!
    elif(n == 2):
        for i in range(n-1):
            if(l[i] == l[i+1]):
                count = 1
            else:
                count = count + 2
        print(count)
        exit()
    
    # For other cases!
    else:
        for i in range(n-1):
            if(l[i] == l[i+1]):
                continue
            else:
                i = i + 1
                count = count + 1
    print(count+1)