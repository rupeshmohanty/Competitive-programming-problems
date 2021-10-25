s1 = input()
s2 = input()
fin = []

for i in s1:
    if i in s2:
        fin.append(i)

fin.sort()
print("".join(str(e) for e in fin))