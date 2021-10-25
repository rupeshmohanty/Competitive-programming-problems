# Problem Link: https://www.geeksforgeeks.org/python-program-to-find-largest-element-in-an-array/
class largestNum:
    def __init__(self,l):
        self._l = l

    def large(self):
        return max(self._l)

ip = list(map(int,input().split()))
l = largestNum(ip)
print(l.large())