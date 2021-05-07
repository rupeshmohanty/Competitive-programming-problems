def removeChar(st,k):
    temp = ""

    for i in range(len(st)):
        if i != k:
            temp += st[i]
    
    return temp

if __name__ == "__main__":
    s = input()
    i = int(input())
    res = removeChar(s,i)
    print(res)