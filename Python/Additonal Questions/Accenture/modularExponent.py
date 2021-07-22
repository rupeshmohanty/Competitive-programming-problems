def modularExponent(b,e,m):
    return b**e % m

if __name__ == "__main__":
    b = int(input())
    e = int(input())
    m = int(input())

    res = modularExponent(b, e, m)
    print(res)