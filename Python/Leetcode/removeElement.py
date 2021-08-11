class Solution:
    def removeElement(self,nums,val):
        res = ""
        for i in range(len(nums)):
            if nums[i] != val:
                res += str(nums[i])
            
        return res
    
nums = [3,2,2,3]
val = 3
ob = Solution()
print(ob.removeElement(nums, val))