def divisors(n):
    res = []    
    for i in range(1,n+1):
        if n % i == 0:
            res.append(i)
    return res

n = int(input())
r = []

r += divisors(n)
print(r)
temp = []

for i in range(1,len(r)+1):
    s = 0    
    for j in range(i):
        s += r[j]
    temp.append(s)

print(sum(temp))