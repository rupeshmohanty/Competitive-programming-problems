if __name__ == '__main__':
    test_list = [2, 4, 5, 2, 5, 4, 2, 4, 5, 7, 7, 8, 3]
    t1 = set(test_list)
    count = 0
    
    for i in t1:
        count += test_list.count(i) // 2

    print(count)
