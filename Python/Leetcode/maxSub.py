class Solution:
    def maxSubArray(self,nums):
        max_sum = nums[0] 
        temp_sum = 0

        i = 0
        while(i < len(nums)):
            temp_sum += nums[i]

            if temp_sum > max_sum:
                max_sum = temp_sum
            
            if temp_sum < 0:
                temp_sum = 0

            i += 1
        
        return max_sum

    
nums = list(map(int, input().split()))
ob = Solution()
print(ob.maxSubArray(nums))
