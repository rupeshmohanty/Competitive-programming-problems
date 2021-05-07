def consecutiveMultiple(l,K):
    main = []
    for i in range(len(l)):
        prod = 1
        if(i+K > len(l)):
            break
        for j in range(i,i+K):
            prod *= l[j]
        main.append(prod)

    return main

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    k = int(input())
    res = consecutiveMultiple(arr,k)
    print(res)
