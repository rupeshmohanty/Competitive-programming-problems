# Question Link: https://practice.geeksforgeeks.org/problems/pangram-checking-1587115620/1/?category[]=Strings&category[]=Strings&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]StringsproblemStatusunsolveddifficulty[]0page1category[]Strings
s = input()
res = set()
s = s.lower()

for i in s:
    if i.isalpha():
        res.add(i)

if len(res) == 26:
    print(1)
else:
    print(0)