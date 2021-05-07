def removeDups(st):
    st = set(st)
    st = sorted(st)
    r = "".join(st)
    return r


if __name__ == "__main__":
    s = input()
    res = removeDups(s)
    print(res)
