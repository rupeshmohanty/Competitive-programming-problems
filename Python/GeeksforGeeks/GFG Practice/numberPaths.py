def numberOfPaths(m,n):
    if m == 1 or n == 1:
        return 1
    
    return numberOfPaths(m,n-1) + numberOfPaths(m-1, n)
    
m,n = map(int,input().split())
res = numberOfPaths(m,n)
print(res)