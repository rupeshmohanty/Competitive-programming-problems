# Question Link: https://edabit.com/challenge/cXnkmRdxqJrwdsP4n
def dis(price,discount):
	price = price - (discount*price/100)

	return price

if __name__ == "__main__":
	p = int(input())
	d = int(input())

	res = dis(p,d)

	print(res)