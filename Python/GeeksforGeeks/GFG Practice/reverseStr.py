s = input()
res = []
t = ""

for i in range(len(s)):
    if s[i] != '.':
        t += s[i]
    else:
        res.append(t)
        t = ""

res.append(t)
fin = ""

for i in range(len(res)-1,0,-1):
    fin += res[i] + "."

fin += res[0]

print(fin)