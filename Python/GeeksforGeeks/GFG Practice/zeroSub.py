n = int(input())
a = list(map(int,input().split()))
count = 0

for i in range(n):
    c0,c1 = 0,0
    for j in range(i):
        if a[j] == 0:
            c0 += 1
        else:
            c1 += 1
    if c0 == c1:
        count += c0

print(count)