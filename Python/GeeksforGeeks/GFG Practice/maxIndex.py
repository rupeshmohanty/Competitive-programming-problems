# Question Link: https://practice.geeksforgeeks.org/problems/minimum-indexed-character0221/1/?category[]=Strings&category[]=Strings&problemStatus=solved&difficulty[]=0&page=1&query=category[]StringsproblemStatussolveddifficulty[]0page1category[]Strings

s = input()
patt = input()
res = 0
flag = False
m = len(s) - 1

for i in range(len(patt)):
    if patt[i] in s:
        res = s.find(patt[i])
        if res < m:
            m = res
        flag = True
  
if(flag):
    print(s[m])
else:
    print("$")