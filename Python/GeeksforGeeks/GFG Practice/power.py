def numRev(n):
    s = ""
    temp = 0

    while n > 0:
        temp = n%10
        s += str(temp)
        n = n//10
    
    return int(s)
    
n = int(input())
rev = numRev(n)
print(pow(n,rev)%1000000007)