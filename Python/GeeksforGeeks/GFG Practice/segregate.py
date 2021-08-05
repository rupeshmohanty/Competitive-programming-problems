# Question Link: https://practice.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]ArraysproblemStatusunsolveddifficulty[]0page1category[]Arrays

n = int(input())
arr = list(map(int,input().split()))
res = []

# adding 0s to the list first!

for i in arr:
    if i == 0:
        res.append(i)

# adding 1s to the list!

for j in arr:
    if j == 1:
        res.append(j)

print(" ".join(str(e) for e in res))        