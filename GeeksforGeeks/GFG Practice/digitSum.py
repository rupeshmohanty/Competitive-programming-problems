n = int(input())
temp = 0
s = 0

while(n > 0):
    temp = n%10
    s += temp
    n = n//10

print(s)