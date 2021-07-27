nums = list(map(int,input().split()))
s1,s2 = 0,0
nums.sort()
n = len(nums)
s1 += nums[n-1]

for i in range(n-1):
    if(s1 > s2):
        s2 += nums[i]
    else:
        break

if(s1 == s2):
    print(True)
else:
    print(False)