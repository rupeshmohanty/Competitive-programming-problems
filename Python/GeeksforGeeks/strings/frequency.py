def frequency(s1):
    d = {}
    for k in s1.split():
        d[k] = s1.count(k)
    
    return d

if __name__ == "__main__":
    st1 = input()
    res = frequency(st1)
    print(res)