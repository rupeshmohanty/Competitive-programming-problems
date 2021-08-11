class Solution:
    def isValid(self,s):
        flag = False
        for i in range(len(s)-1):
            if s[i] == '(' and s[i+1] == ')' or s[i] == '[' and s[i+1] == ']' or s[i] == '{' and s[i+1] == '}':
                flag = True
            else:
                flag = False
        
        if flag:
            return True
        else:
            return False

s = input()
ob = Solution()
print(ob.isValid(s))