if __name__ == '__main__':
    s = input()
    res = []

    for i in range(len(s)):
        temp = 0
        temp = s.count(s[i])
        if (temp,s[i]) not in res:
            res.append((temp,s[i]))
    
    res.sort(reverse=True)
    for j in range(3):
        print(res[j][1],res[j][0])
        