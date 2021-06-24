if __name__ == "__main__":
    n = int(input())
    s = input().split()
    res = []

    res.append(s[0])

    i = 1
    while(i > 0):
        res.append(s[i])
        i += 1

        s.remove(s[i])
    
    print(res)