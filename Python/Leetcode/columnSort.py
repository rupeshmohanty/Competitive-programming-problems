strs = list(map(str,input().split()))
count = 0

for i in range(len(strs)):
    flag = True
    for j in range(len(strs[i])-1):
        if strs[i][j] >= strs[i][j+1]:
            flag = False
            break
    
    if flag == False:
        count += 1

print(count)
