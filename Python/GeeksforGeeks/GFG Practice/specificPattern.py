# Question Link: https://practice.geeksforgeeks.org/problems/match-specific-pattern/1/?category[]=Strings&category[]=Strings&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]StringsproblemStatusunsolveddifficulty[]0page1category[]Strings
n = int(input())
d = list(map(str, input().split()))
pattern = input()
res1 = []
fin = []

for i in pattern:
    res.append(pattern.count(i))

for i in d:
    res2 = []
    for j in i:
        res2.append(i.count(j))

        if res1 == res2:
            fin.append(j)
        else:
            continue

print(" ".join(fin))
