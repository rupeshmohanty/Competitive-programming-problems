class Solution:
    def longestCommonPrefix(self,strs):
        res = ""

        for i in range(len(strs)):
            temp = strs[i][i]
            flag = False
            for j in range(len(strs)):
                if i != j:
                    if strs[j][i] == temp:
                        flag = True
                    else:
                        flag = False
                
            if flag:
                res += strs[i][i]
            
        return res

s = list(map(str,input().split()))
ob = Solution()
print(ob.longestCommonPrefix(s))