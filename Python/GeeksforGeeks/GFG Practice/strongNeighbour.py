# Question Link: https://www.geeksforgeeks.org/python-program-to-find-the-strongest-neighbour/
arr = list(map(int, input().split()))
res = []

for i in range(len(arr)-1):
    if arr[i+1] > arr[i]:
        res.append(arr[i+1])
    else:
        res.append(arr[i])

print(" ".join(str(e) for e in res)) 