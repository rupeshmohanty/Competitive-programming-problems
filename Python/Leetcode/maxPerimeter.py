nums = list(map(int,input().split()))
nums.sort()
res = []

for i in range(len(nums)-2):
    if nums[i] + nums[i+1] > nums[i+2]:
        res.append(nums[i]+nums[i+1]+nums[i+2])

if len(res) > 0:
    print(max(res))
else:
    print(0)