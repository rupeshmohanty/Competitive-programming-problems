arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
res = []

for i in arr2:
    if i in arr1:
        res += [i]*arr1.count(i)

temp = []
for k in arr1:
    if k not in res:
        temp.append(k)

temp.sort()
print(res+temp)