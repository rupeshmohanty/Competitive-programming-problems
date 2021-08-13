class Solution:
    def threeSum(self,nums):
        if len(nums) == 0:
            return []

        x = nums[0]
        res = []

        for i in range(1,len(nums)):
            y = nums[i]
            for j in range(i+1,len(nums)):
                z = nums[j]

                if x + y + z == 0:
                    res.append([x,y,z])
            
        arr = []

        for i in res:
            if i not in arr:
                arr.append(i)
        
        return arr

nums = list(map(int, input().split()))
ob = Solution()
print(ob.threeSum(nums))