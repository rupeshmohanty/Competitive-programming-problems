# Question Link: https://practice.geeksforgeeks.org/problems/counts-zeros-xor-pairs0349/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]ArraysproblemStatusunsolveddifficulty[]0difficulty[]1page1category[]Arrays

arr = list(map(int,input().split()))
count = 0

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] ^ arr[j] == 0:
            count += 1

print(count)