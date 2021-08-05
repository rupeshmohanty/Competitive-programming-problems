nums = list(map(int,input().split()))
k = int(input())
d = {nums[i]:0 for i in range(len(nums))}
res = []

for i in range(len(nums)):
    d[nums[i]] += 1


