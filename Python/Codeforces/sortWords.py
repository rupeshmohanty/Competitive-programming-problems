def sortWords(l):
    l.sort()
    r = ','.join(l)
    return r

if __name__ == "__main__":
    arr = list(map(str,input().split(',')))
    res = sortWords(arr)
    print(res)