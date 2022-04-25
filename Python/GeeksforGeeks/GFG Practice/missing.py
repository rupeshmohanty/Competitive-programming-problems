n = int(input())
A = list(map(int, input().split()))

res = 0

for i in range(1,n+1):
    if i not in A:
        res = i
        break

print(res)