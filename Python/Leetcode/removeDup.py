# Question Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
class Solution:
    def removeDuplicates(self,nums):
        res = set(nums)
        for i in range(len(nums)):
            nums.pop()
        
        nums += list(res)
        nums.sort()

nums = [0,0,1,1,1,2,2,3,3,4]
ob = Solution()
ob.removeDuplicates(nums)
print(nums)
