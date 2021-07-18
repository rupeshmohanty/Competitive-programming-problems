def redundancy(l):
    main = []
    for i in l:
        total = len(i)
        r = countRepeats(i)
        c = 1 - (r/total)
        main.append(c)

    return main

def countRepeats(a):
    temp = []

    for sub in a:
        if sub not in temp:
            temp.append(sub)

    return len(temp)

if __name__ == '__main__':
    arr = [[4, 5, 2, 4, 3], [5, 5, 5, 5, 5], [8, 7, 8, 8, 7], [1, 2, 3, 4, 5]]
    res = redundancy(arr)
    print(res)
