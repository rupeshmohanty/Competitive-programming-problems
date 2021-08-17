N = int(input())
A = list(map(int,input().split()))
d = {}

for i in range(N):
    if A[i] in d:
        d[A[i]] += 1
    else:
        d[A[i]] = 1

max_count = 0
res = 0
for i in d:
    if d[i] > N//2:
        max_count = d[i]
        res = i 

if max_count == 0:
    print(-1)
else:
    print(res)