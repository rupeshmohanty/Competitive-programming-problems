nums = list(map(int,input().split()))

i = 0
j = len(nums) - 1
c = 0

while(i < len(nums) // 2  and j >= len(nums) // 2):
    if nums[j] < nums[i]:
        nums[j],nums[i] = nums[i],nums[j]
        c += 1
    else:
        j -= 1

    i += 1

print(c)