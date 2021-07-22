# Accenture previous year questions!
def FindAutoCount(n):
    count0 = n.count('0')
    count1 = n.count('1')
    l = list(n)

    if int(n[0]) == count0 and int(n[1]) == count1:
        return len(set(l))
    else:
        return 0

if __name__ == "__main__":
    s = input()
    res = FindAutoCount(s)
    print(res)

