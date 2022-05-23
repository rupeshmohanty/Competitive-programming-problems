words = list(map(str,input().split()))
d = []

for i in words[0]:
    flag = 0
    for j in words[1:]:
        if i not in j:
            flag = 0
            break
        else:
            flag = 1
    
    if flag:
        d.append(i)

print(d)