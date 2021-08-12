class Solution:
    def searchInsert(self,nums,target):
        m = 0
        for i in range(len(nums)):
            if target > nums[i]:
                if i >= m:
                    m = i+1
        
        print(m)

arr = [1,3,5,6]
val = 2
ob = Solution()
ob.searchInsert(arr, val)