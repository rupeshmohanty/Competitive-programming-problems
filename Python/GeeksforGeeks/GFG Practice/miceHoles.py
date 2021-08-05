# Question Link: https://practice.geeksforgeeks.org/problems/assign-mice-holes3053/1/?category[]=Mathematical&category[]=Mathematical&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]MathematicalproblemStatusunsolveddifficulty[]0difficulty[]1page1category[]Mathematical

n = int(input())
m = list(map(int,input().split()))
h = list(map(int,input().split()))
mx = 0

m.sort()
h.sort()

for i in range(n):
    if abs(m[i] - h[i]) > mx:
        mx = abs(m[i] - h[i])

print(mx)