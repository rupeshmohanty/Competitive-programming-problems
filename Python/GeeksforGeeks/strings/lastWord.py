def lastWord(st):
    return st[len(st)-1]

if __name__ == "__main__":
    s = input().split()
    res = lastWord(s)
    print(res)