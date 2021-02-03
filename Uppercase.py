def uppercase(l,K):
    main = []
    for sub in l:
        if(len(sub) > K):
            sub = sub.upper()
        main.append(sub)

    return main

if __name__ == '__main__':
    arr = list(input().split())
    k = int(input())
    res = uppercase(arr,k)
    print(res)
