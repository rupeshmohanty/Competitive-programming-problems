for i in range(int(input())):
    a = input()
    l,r = 0,0
    c = 0

    i = 0
    j = len(a) - 1
    while i < len(a) and j != -1:
        l += int(a[i])
        r += int(a[j])
        c += 2

        if l == r:
            break

        i += 1
        j -= 1
    
    print(c)