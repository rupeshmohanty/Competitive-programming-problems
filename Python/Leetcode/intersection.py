arr = [[1,2,3],[4,5,6]]
res = []
flag = False

for i in arr[0]:
    for j in range(1,len(arr)):
        if i in arr[j]:
            flag = True
        else:
            flag = False
            break
    
    if flag:
        res.append(i)

res.sort()
if len(arr) == 1:
    print(arr[0])
else:
    print(res)
