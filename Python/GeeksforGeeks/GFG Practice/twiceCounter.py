# Question Link: https://practice.geeksforgeeks.org/problems/twice-counter4236/1/?category[]=Strings&category[]=Strings&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]StringsproblemStatusunsolveddifficulty[]0page1category[]Strings
n = int(input())
l = list(map(str, input().split()))
s = set(l)
count = 0

for i in s:
    if l.count(i) == 2:
        count += 1
    
print(count)