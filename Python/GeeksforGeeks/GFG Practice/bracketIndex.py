# Question Link: https://practice.geeksforgeeks.org/problems/closing-bracket-index5900/1/?category[]=Strings&category[]=Strings&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]StringsproblemStatusunsolveddifficulty[]0category[]Stringspage1#
s = input()
count = 0
pos = int(input())

for i in range(pos,len(s)):
    if s[i] == '[':
        count += 1
    elif s[i] == ']':
        count -= 1
    
    if count == 0:
        print(i)
        break