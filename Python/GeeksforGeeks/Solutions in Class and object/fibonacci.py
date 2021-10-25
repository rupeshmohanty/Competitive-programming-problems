# Problem Link: https://www.geeksforgeeks.org/python-program-for-n-th-fibonacci-number/
class fibonacci:
    def __init__(self,x):
        self._x = 1

    def findFibo(self,x):
        self._x = x

        if self._x <= 0:
            print("Incorrect Input")
        elif self._x == 1:
            return 0
        elif self._x == 2:
            return 1
        else:
            return self.findFibo(self._x-1) + self.findFibo(self._x-2)

n = int(input())
f = fibonacci(n)
x = f.findFibo(n)
print(x)