# Question Link: https://www.geeksforgeeks.org/python-program-to-check-if-the-list-contains-three-consecutive-common-numbers-in-python/
arr = list(map(int, input().split()))
count = 0
res = []

for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        count += 1
    else:
        count = 0
    
    if count == 2:
        res.append(arr[i])
        count = 0

print(" ".join(str(e) for e in res))


   