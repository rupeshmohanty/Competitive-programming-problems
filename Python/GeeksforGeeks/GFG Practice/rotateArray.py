# Question Link: https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]ArraysproblemStatusunsolveddifficulty[]0difficulty[]1page1category[]Arrays#

n,d = map(int,input().split())
arr = list(map(int,input().split()))
res = []

for i in range(d):
    res.append(arr[i])

for i in res:
    if i in arr:
        arr.remove(i)

print(arr + res)
