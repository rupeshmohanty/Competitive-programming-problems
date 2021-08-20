n = int(input())
arr = list(map(int, input().split()))
res = []

while(len(arr) != 0):
    if len(arr) == 1:
        res.append(arr[0])
        arr.pop()
    else:
        res.append(arr[len(arr)-1])
        res.append(arr[0])

        arr.pop()
        arr.pop(0)

arr += res
print(arr)

