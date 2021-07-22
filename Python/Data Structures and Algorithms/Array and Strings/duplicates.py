s = input()
res = []

for i in range(len(s)):
    if s.count(s[i]) > 1:
        res.append(s[i],s.count(s[i]))

for j in res:
    print(j[0],"count=",j[1])