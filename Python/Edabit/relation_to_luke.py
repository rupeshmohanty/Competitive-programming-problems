# Question Link: https://edabit.com/challenge/8pDH2SRutPoaQghgc

rel = {"Darth Vader": "father", "Leia": "sister","Han": "brother in law","R2D2": "droid"}

def relation_to_luke(st):
	return rel[st]

if __name__ == "__main__":
	s = input()
	res = relation_to_luke(s)

	print(f'Luke, I am your { res }')