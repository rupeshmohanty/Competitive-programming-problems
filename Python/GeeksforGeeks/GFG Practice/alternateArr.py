n = int(input())
arr = list(map(int, input().split()))
temp = []
m,m1 = 0,0

for i in range(len(arr)):
    if i % 2 == 0:
        m = max(arr)
        temp.append(m)
        arr.pop(i)
    else:
        m1 = min(arr)
        temp.append(m1)
        arr.pop(i)

print(temp)