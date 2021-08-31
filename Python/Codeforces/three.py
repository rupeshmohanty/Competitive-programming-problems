for i in range(int(input())):
    k = int(input())
    c = 0

    j = 1
    while True:
        if j % 3 != 0 and j % 10 != 3:
            k -= 1
        
        if k == 0:
            print(j)
            break
    
        j += 1