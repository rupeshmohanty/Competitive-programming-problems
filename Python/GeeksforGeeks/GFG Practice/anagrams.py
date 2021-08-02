def findAnagrams(s,l):
    res = []
    for i in l:
        a = list(s)
        b = list(i)

        if a.sort() == b.sort():
            res.append(s)
            res.append(i)
    
    return [res]

if __name__ == "__main__":
    n = int(input())
    words = list(map(str, input().split()))
    res = []

    for i in words:
        if [i] not in res:
            res += findAnagrams(i,words)

    print(res)