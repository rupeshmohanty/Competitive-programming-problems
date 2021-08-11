n1 = int(input())
n2 = int(input())
count = 0

for i in range(n1,n2+1):
    res = []
    temp = 0
    while(i > 0):
        temp = i % 10
        res.append(temp)
        i = i // 10
    if len(set(res)) == len(res):
        count += 1

if count == 0:
    print("No unique numbers")
else:
    print(count)