import math

n,k = map(int,input().split())
num = pow(n,k)
res = []

while(num**(1/k) < n + 1):
    res.append(num)    
    num += 1


    