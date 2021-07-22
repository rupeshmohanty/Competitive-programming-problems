# Accenture previous year questions!
def FrequentCharacterReplaced(s,x):
    freq = ""
    maxm = 0
    r = ""

    for i in range(len(s)):
        if s.count(s[i]) > maxm:
            freq = s[i]
            maxm = s.count(s[i])

    for i in range(len(s)):
        if s[i] == freq:
            r += x
        else:
            r += s[i]

    return r

if __name__ == "__main__":
    a = input()
    c = input()

    res = FrequentCharacterReplaced(a, c)
    print("".join(str(e) for e in res))