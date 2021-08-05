# Question Link: https://practice.geeksforgeeks.org/problems/find-maximum-number2152/1/?category[]=Mathematical&category[]=Mathematical&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]MathematicalproblemStatusunsolveddifficulty[]0difficulty[]1page1category[]Mathematical#

n = input()
res = []

for i in n:
    res.append(int(i))

res.sort(reverse=True)

print("".join(str(e) for e in res))