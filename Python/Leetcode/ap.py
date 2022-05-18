arr = list(map(int,input().split()))
arr.sort()
flag = True
d = arr[1] - arr[0]

for i in range(len(arr)-1):
    if arr[i+1] - arr[i] != d:
        flag = False
        break

print(flag)