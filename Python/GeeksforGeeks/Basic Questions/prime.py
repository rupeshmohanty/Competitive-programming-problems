n = int(input())
res = False

for i in range(2,n):
    if n % i == 0:
        res = True

if(res):
    print("Not a prime number")
else:
    print("Prime number")    