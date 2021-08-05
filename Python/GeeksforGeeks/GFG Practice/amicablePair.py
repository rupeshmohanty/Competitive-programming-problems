# Question Link: https://practice.geeksforgeeks.org/problems/amicable-pair0804/1/?category[]=Mathematical&category[]=Mathematical&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]MathematicalproblemStatusunsolveddifficulty[]0difficulty[]1page1category[]Mathematical

def divisors(a,b):
    res1 = []
    res2 = []
    for i in range(1,a):
        if a % i == 0:
            res1.append(i)
    
    for j in range(1,b):
        if b % j == 0:
            res2.append(j)

    if sum(res1) == b and sum(res2) == a:
        return 1
    else:
        return 0

A,B = map(int,input().split())
res = divisors(A,B)
print(res)
