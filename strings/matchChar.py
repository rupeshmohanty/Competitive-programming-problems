def matchChar(str1,str2):
    count = 0
    r = []
    for i in str1:
        if i not in r:
            if i in str2:
                count = count + 1
                r.append(i)
    
    return count

if __name__ == "__main__":
    s1 = input()
    s2 = input()

    res = matchChar(s1,s2)
    print(res)