class Solution:
    def findDuplicate(self, nums):
        res = []
        for i in range(len(nums)):
            if nums[i] == "," or nums[i] == "[" or nums[i] == "]":
                continue
            else:
                if nums[i] in res:
                    return nums[i]
                res.append(nums[i])
        
if __name__ == "__main__":
    n = input()
    sol = Solution()
    res = sol.findDuplicate(n)
    print(res)