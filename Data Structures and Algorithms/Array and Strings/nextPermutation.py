nums = list(map(int, input().split()))
count = 0

for i in range(len(nums)-1,0,-1):
    if nums[i-1] < nums[i]:
        (nums[i-1],nums[i]) = (nums[i],nums[i-1])
    else:
        count += 1

if count > 0:
    print(sorted(nums))
else:
    print(nums)