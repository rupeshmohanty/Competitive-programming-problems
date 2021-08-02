# Question Link: https://practice.geeksforgeeks.org/problems/remove-duplicates3034/1/?category[]=Strings&category[]=Strings&difficulty[]=0&page=1&query=category[]Stringsdifficulty[]0category[]Stringspage1
s = input()
t = []

for i in s:
    if i not in t:
        t.append(i)

print(" ".join(str(e) for e in t)) 