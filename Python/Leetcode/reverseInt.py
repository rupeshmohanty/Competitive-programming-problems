class Solution:
    def reverse(self,x):
        s = str(abs(x))
        t = s[::-1]

        if x > 0:
            if int(t) > 2**31 - 1:
                return 0
            else:
                return int(t)
        else:
            if -1*int(t) < -2**31:
                return 0
            else:
                return -1*int(t)


ob = Solution()
x = int(input())
print(ob.reverse(x))