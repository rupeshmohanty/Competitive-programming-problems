def evenLength(st):
    r = ""

    for i in st:
        if(len(i) % 2 == 0):
            r = r + i

    return r

if __name__ == "__main__":
    s = input().split()
    res = evenLength(s)
    print(res)