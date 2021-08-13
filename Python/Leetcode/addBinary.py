class Solution:
    def addBinary(self,a,b):
        x,y = 0,0

        i = len(a) - 1
        j = 0
        while(i != -1):
            x += pow(2,j)*int(a[i])
            i -= 1
            j += 1
        
        i = len(b) - 1
        j = 0
        while(i != -1):
            y += pow(2,j)*int(b[i])
            i -= 1
            j += 1
        
        temp = ""
        temp = bin(x+y)

        temp = temp.replace("0b","")

        return temp

a = input()
b = input()
ob = Solution()
print(ob.addBinary(a,b))
