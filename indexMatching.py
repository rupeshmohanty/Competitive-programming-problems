def indexMatching(t1,t2,K):
    r = []
    for i in range(len(t1)):
        if t1[i][K] == t2[i][K]:
            r.append(t1[i])
            r.append(t2[i])

    return r

if __name__ == '__main__':
    test_list1 = [[1, 8, 3], [9, 2, 0], [6, 4, 4], [6, 4, 4]]
    test_list2 = [[1, 9, 3], [8, 2, 3], [5, 4, 6], [5, 4, 6]]

    k = int(input())

    res = indexMatching(test_list1,test_list2,k)
    print(res)
