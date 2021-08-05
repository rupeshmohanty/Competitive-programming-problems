# Question Link: https://practice.geeksforgeeks.org/problems/akaashs-assignment0828/1/?category[]=Mathematical&category[]=Mathematical&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]MathematicalproblemStatusunsolveddifficulty[]0difficulty[]1page1category[]Mathematical#

import math

n,k = map(int,input().split())
num = pow(n,k)
num1 = pow(n+1,k)

print(num1-num)

    