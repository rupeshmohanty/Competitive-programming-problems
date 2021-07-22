def delimiters(t1,t2,d):
    r = []

    for i in d:
        temp = ""
        temp = temp + t1 + i + t2
        r.append(temp)
    
    return r

if __name__ == "__main__":
    test_str1 = input()
    test_str2 = input()
    d_list = ["+","*","-","$",",","@"]

    res = delimiters(test_str1,test_str2,d_list)
    print(res)