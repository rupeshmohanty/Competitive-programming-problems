# Question Link: https://www.geeksforgeeks.org/python-list-product-excluding-duplicates/
arr = list(map(int,input().split()))
res = []
prod = 1

for i in range(len(arr)):
    if arr[i] not in res:
        prod *= arr[i]
        res.append(arr[i])

print(prod)
