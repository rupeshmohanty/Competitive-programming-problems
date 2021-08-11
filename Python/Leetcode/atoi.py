class Solution:
    def myAtoi(self, s: str) -> int:
        t = ""
        
        for i in s:
            if i.isalpha():
                break                
            elif i.isspace():
                continue
            else:
                t += i
        
        if t == "":
            return 0
        else:
            return int(t)

ob = Solution()
st = input()
print(ob.myAtoi(st))