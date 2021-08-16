s = input()
count1 = 1
res = list()
fin = []

for i in range(len(s)):
    if s[i] == '(':
        fin.append(count1)
        res.append(count1)
        count1 += 1
    elif s[i] == ')':
        fin.append(res[-1])
        res.pop()
    
print(" ".join(str(e) for e in fin))

