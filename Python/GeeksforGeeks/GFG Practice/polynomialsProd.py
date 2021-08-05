# Question Link: https://practice.geeksforgeeks.org/problems/multiply-two-polynomals0721/1/?category[]=Mathematical&category[]=Mathematical&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]MathematicalproblemStatusunsolveddifficulty[]0difficulty[]1page1category[]Mathematical

m,n = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
fin = [0] * (m+n-1)

for i in range(m):
    for j in range(n):
        fin[i+j] += arr1[i]*arr2[j]

print(fin)        