class Solution:
    def lengthOfLastWord(self,s):
        res = s.split(" ")
        t = ""
        fin = []

        for i in res:
            if i != '':
                fin.append(i)
        
        return len(fin[-1])

s = input()
ob = Solution()
print(ob.lengthOfLastWord(s))
