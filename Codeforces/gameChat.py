t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    count = 0

    for i in range(n):
        if s[i] == ')':
            count += 1
        else:
            count = 0
    
    if count > (n - count):
        print("Yes")
    else:
        print("No")