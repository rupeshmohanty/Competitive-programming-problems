class Solution:
    def plusOne(self,digits):
        t = ""
        
        for i in digits:
            t += str(i)
        
        x = int(t) + 1
        res = []

        for i in str(x):
            res.append(int(i))
        
        return res

arr = [1,2,3]
ob = Solution()
print(ob.plusOne(arr))