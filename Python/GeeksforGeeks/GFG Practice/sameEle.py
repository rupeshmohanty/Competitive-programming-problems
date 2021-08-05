n = int(input())
arr = list(map(int,input().split()))
dist = 0

for i in range(n):
    temp = arr[i]
    max = i
    min = i
    for j in range(n):
        if arr[j] == temp:
            if j > max:
                max = j
    if max - min > dist:
        dist = max - min

print(dist)    