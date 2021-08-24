class Solution:
    c = 2
    def isLucky(self,n):
        if self.c > n:
            self.c = 2
            return 1
        
        if n % self.c == 0:
            self.c = 2
            return 0
        
        n = n - (n//self.c)
        self.c += 1
        return self.isLucky(n)


ob = Solution()
n = int(input())
print(ob.isLucky(n))