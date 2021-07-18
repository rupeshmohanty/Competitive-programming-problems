n = int(input())
arr = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i,n):
        if arr[j] < arr[i]:
            count += 1
    
print(count)
