# Question Link: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#
n = int(input())
start = list(map(int,input().split()))
finish = list(map(int, input().split()))
count = 0

for i in range(n):
    if i == 0:
        pass
    else:
        if(abs(start[i] - finish[i]) <= abs(start[i-1] - finish[i-1])):
            count += 1

print(count)