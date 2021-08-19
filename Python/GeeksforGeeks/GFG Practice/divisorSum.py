class Solution:
    def divisors(self,num):
        s = 0
        for i in range(1,num+1):
            if num % i == 0:
                s += i
        
        return s

    def sumOfDivisors(self, N):
        fac = []

        for i in range(1,N+1):
            if N % i == 0:
                fac.append(i)
        
        final_sum = 0

        for i in fac:
            s = self.divisors(i)
            final_sum += s

        return final_sum 
        
n = int(input())
ob = Solution()
print(ob.sumOfDivisors(n))
