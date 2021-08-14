class Solution:
    def majorityElement(self,nums):
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        
        for i in dic.keys():
            if dic[i] > len(nums)//2:
                return i

nums = list(map(int, input().split()))
ob = Solution()
print(ob.majorityElement(nums))