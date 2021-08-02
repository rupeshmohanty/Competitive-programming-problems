# Question Link: https://practice.geeksforgeeks.org/problems/check-if-the-number-is-balanced3014/1/?category[]=Strings&category[]=Strings&problemStatus=solved&difficulty[]=0&page=1&query=category[]StringsproblemStatussolveddifficulty[]0page1category[]Strings
s = input()

left_sum = 0
right_sum = 0

for i in range(len(s)//2):
    left_sum += int(s[i])
    right_sum += int(s[len(s) - i - 1])

if left_sum == right_sum:
    print(1)
else:
    print(0)