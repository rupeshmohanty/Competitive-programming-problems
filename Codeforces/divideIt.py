q = int(input())

for _ in range(q):
    n = int(input())
    count = 0

    while(n > 1):
        if n % 5 == 0:
            n = int(4*(n//5))
            count += 1
        elif n % 3 == 0:
            n = int(2*(n//3))
            count += 1
        elif n % 2 == 0:
            n = int(n//2)
            count += 1
        else:
            count = -1
            break
    
    print(count)