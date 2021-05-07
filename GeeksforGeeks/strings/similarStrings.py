def similarStrings(t1,t2,d):
    count1, count2 = 0,0
    
    for i in t1:
        for j in t2:
            if(i == j):
                count1 = t1.count(i)
                count2 = t2.count(j)

        if(count1 - count2 <= d):
            return True
            break
        else:
            return False 

if __name__ == "__main__":
    test_str1 = input()
    test_str2 = input()
    k = int(input())
    res = similarStrings(test_str1,test_str2,k)
    print(res)