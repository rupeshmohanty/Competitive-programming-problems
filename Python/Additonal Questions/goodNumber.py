import math

def goodcheck(n):
    k=math.floor(math.log(n,3))
    while k>=0 and n!=0:
        if n>=3**k:
            n=n-3**k
        k-=1
    if n==0:
        return True
    else:
        return False

N=int(input())
j=0

while True:
    k=N+j
    if goodcheck(k):
        print(k)
        break
    j+=1