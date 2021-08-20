n = int(input())
A = list(map(int, input().split()))
res = []

m = -1
for i in range(n-1,-1,-1):
    if A[i] >= m:
        m = A[i]
        res.append(A[i])
    
print(res[::-1])