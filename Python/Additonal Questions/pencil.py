def fact(num):
    fact = 1

    while num > 0:
        fact *= num
        num -= 1
    
    return fact

n = int(input())
m = int(input())
p = int(input())
e = int(input())

res = fact(n)/fact(n-p)*fact(p) * fact(m)/fact(m-e)*fact(e)
print(int(res))