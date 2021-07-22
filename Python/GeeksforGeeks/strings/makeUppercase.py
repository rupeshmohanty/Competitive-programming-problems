def makeUppercase(t,d):
    for i in range(len(t)):
        if len(t[i]) > d:
            t[i] = t[i].upper()

    return t

if __name__ == "__main__":
    test_list = ["Gfg", "is", "best", "for", "geeks"]
    k = int(input())
    res = makeUppercase(test_list,k)
    print(res)