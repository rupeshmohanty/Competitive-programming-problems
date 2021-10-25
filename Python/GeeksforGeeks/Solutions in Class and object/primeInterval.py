# Problem Link: https://www.geeksforgeeks.org/python-program-to-print-all-prime-numbers-in-an-interval/
class primeInterval:
    def __init__(self,a,b):
        self._a = a
        self._b = b

    def checkPrime(self,x):
        self._x = x
        
        for i in range(2,self._x):
            if self._x % i == 0:
                return False
        
        return True

    def interval(self):
        primes = []
        for i in range(self._a,self._b):
            if(self.checkPrime(i)):
                primes.append(i)
        
        return primes

x,y = map(int,input().split())
p = primeInterval(x, y)
l = p.interval()
print(l)