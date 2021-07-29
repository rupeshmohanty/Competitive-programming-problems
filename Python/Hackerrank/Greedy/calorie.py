# Question Link: https://www.hackerrank.com/challenges/marcs-cakewalk/problem?h_r=next-challenge&h_v=zen

n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
s = 0

for i in range(n):
    s += pow(2,i)*arr[i]

print(s)