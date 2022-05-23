nums = [-8,7,-1,3,5,7,-8,-8,0]
d = []

for i in nums:
    if (i,nums.count(i)) not in d:
        d.append((i,nums.count(i)))

d.sort(key=lambda x:x[1])
res = []

for k in range(len(d)-1):
    if d[k][1] == d[k+1][1]:
        if d[k+1][0] > d[k][0]:
            d[k+1],d[k] = d[k],d[k+1]

print(d)
for a in d:
    res += [a[0]]*a[1]

print(res) 