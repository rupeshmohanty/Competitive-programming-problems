n = int(input())
arr = list(map(int, input().split()))
prod = 1
m = 0
s = set()

for i in range(n):
    prod *= arr[i]

    if prod > m and prod not in s:
        m = prod
        s.add(prod)
    else:
        continue
    
print(s)