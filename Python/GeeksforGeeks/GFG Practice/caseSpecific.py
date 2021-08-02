n = int(input())
s = input()
upper = []
lower = []
res = ""

for i in s:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    else:
        pass

lower.sort()
upper.sort()

for i in range(len(s)//2):
    if s[i].islower():
        res += lower[i]
    elif s[i].isupper():
        res += upper[i]
    else:
        pass

print(res)

    