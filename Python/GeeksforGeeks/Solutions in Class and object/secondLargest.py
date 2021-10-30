# Question Link: https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/
class secondLargest:
	def __init__(self,l):
		self._l = l

	def findSecondLargest(self):
		m = max(self._l)
		self._l.remove(m)

		new_m = max(self._l)

		return new_m

if __name__ == "__main__":
	l = list(map(int,input().split()))
	s = secondLargest(l)
	print(s.findSecondLargest())