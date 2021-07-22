def checkFactor(num):
    for i in range(2,num):
        if num % i == 0:
            return i

a,b = map(int,input().split())
s = a
flag = False
res = 0

i = 1
while(i <= a):
    res = checkFactor(s)
    s += res

    if s == b:
        flag = True
        break
    i += 1

if flag:
    print("Yes")
else:
    print("No")