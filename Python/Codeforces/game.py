n = int(input())
arr = []

for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))

count = 0

for i in range(n):
    for j in range(n):
        if i != j:
            if arr[i][1] == arr[j][0]:
                count += 1

print(count)