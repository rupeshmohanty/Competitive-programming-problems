a = [0,1]
temp = 0
count = 0

for i in range(2,100):
    temp = a[i-1] + a[i-2]
    a.append(temp)

n = int(input())

for i in a:
    if(n == i):
        count = count + 1
        break
    else:
        count = 0

if(count != 0):
    print("YES")
else:
    print("NO")