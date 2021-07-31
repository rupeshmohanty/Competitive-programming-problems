n = int(input())
arr = []
profit = 0
count = 0
m = 0

# inserting tuples!
for i in range(n):
    a,b,c = map(int, input().split())
    arr.append((a,b,c))

# sorting the tuples based on the deadlines!
for i in range(n):
    for j in range(n-1):
        if arr[j][1] <= arr[j+1][1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

last_index = 0
last_profit = 0

for i in range(n):
    if arr[i][1] >= m:
        m = arr[i][1]

    if arr[i][1] >= m:
        profit += arr[i][2]
        count += 1
        last_index = i
        last_profit = arr[i][2]

for i in range(last_index+1,n):
    if arr[i][2] > last_profit:
        last_profit = arr[i][2]
        count += 1

print(count,last_profit+profit)