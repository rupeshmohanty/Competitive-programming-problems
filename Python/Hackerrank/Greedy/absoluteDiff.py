# Question link: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = abs(arr[1] - arr[0])

for i in range(1,n):
    if abs(arr[i] - arr[i-1]) < m:
        m = abs(arr[i] - arr[i-1])

print(m)