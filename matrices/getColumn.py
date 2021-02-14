def getColumn(l):
    res = []
    for i in range(len(l)):
        res.append(l[i][len(l[i]) - 1])

    return res 

if __name__ == "__main__":
    test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
    r = getColumn(test_list)
    print(r)