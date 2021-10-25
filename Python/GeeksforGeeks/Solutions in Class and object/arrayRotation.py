# Program Link: https://www.geeksforgeeks.org/python-program-for-program-for-array-rotation-2/
class arrayRotation:
    def __init__(self,n,d,l):
        self._n = n
        self._d = d
        self._l = l

    def rotate(self):
        temp = []

        for i in range(self._d,self._n):
            temp.append(self._l[i])
        
        for i in range(self._d):
            temp.append(self._l[i])
        
        return temp
        

n,d = map(int,input().split())
l = list(map(int,input().split()))
a = arrayRotation(n, d, l)
print(a.rotate())
