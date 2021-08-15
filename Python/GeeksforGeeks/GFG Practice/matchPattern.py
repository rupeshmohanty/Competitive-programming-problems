n = int(input())
d = list(map(str,input().split()))
pattern = input()
temp = []
fin = []

for i in pattern:
    temp.append(pattern.count(i))

for j in d:
    t = []
    for i in j:
        t.append(j.count(i))
    
    if t == temp:
        fin.append(j)

print(fin)

