class Solution:
    def romanToInt(self,s):
        d = {'I':'1','V':'5','X':'10','L':'50','C':'100','D':'500','M':'1000'}
        t = 0

        for i in range(len(s)-1):
            if int(d[s[i]]) < int(d[s[i+1]]):
                t -= int(d[s[i]])
            else:
                t += int(d[s[i]])
        
        t += int(d[s[len(s)-1]])

        return t
s = input()
ob = Solution()
print(ob.romanToInt(s))