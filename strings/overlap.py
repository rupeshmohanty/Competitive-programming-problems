def overlap(st1,st2):
    for char in range(len(st1)):
        if st2.startswith(st1[char:]):
            r = st1[char:]
            break
    
    return r

if __name__ == "__main__":
    s1 = input()
    s2 = input()

    res = overlap(s1,s2)
    print(res)