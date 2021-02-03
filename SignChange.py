def signChange(l):
    main = []
    for i in l:
        main.append((abs(i[0]),-abs(i[1])))

    return main

if __name__ == '__main__':
    arr = [(3, -1), (-4, -3), (1, 3), (-2, 5), (-4, 2), (-9, -3)]
    res = signChange(arr)
    print(res)
