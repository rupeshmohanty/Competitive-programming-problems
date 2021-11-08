def primeInterval(s,e):
	prime = []
	for i in range(s,e):
		if checkPrime(i):
			prime.append(i)

	return prime


def checkPrime(num):
	for i in range(2,num):
		if num % i == 0:
			return False

	return True

if __name__ == "__main__":
	s,e = map(int,input().split())
	res = primeInterval(s,e)

	for i in res:
		print(i)