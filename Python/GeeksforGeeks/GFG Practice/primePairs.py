def checkPrime(num):
    count = 0    
    for i in range(2,num):
        if num % i == 0:
            count += 1
    if count > 0:
        return False
    else:
        return True 

n = int(input())
m = int(input())
res = False
l = []

for i in range(n,m):
    res = checkPrime(i)
    if(res):
        l.append(i)

c = 0
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[j] - l[i] == 6:
            c += 1

if c == 0:
    print("No prime pairs")
else:
    print(c)
    
        