first = "qwertyuiop"
second = "asdfghjkl"
third = "zxcvbnmm"
res = []

words = ["adsdf","sfd"]

for i in words:
    f1,f2,f3 = 0,0,0
    for j in i:
        if j.lower() in first:
            f1 += 1
        elif j.lower() in second:
            f2 += 1
        elif j.lower() in third:
            f3 += 1

    if f1 == len(i) or f2 == len(i) or f3 == len(i):
        res.append(i)

print(res)