arr = list(map(int, input().split()))
pre = []
temp = 0

for i in range(len(arr)):
    temp += arr[i]
    pre.append(temp)

print(pre)