def uncommonWords(st1,st2):
    r = []

    r = list(set(st1) ^ set(st2))
    
    return r

if __name__ == "__main__":
    s1 = input().split()
    s2 = input().split()

    res = uncommonWords(s1,s2)
    print(res)