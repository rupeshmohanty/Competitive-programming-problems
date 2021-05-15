def numberDigits(X):
    c = 0

    while(X > 0):
        temp = X%10
        c = c + 1
        X = int(X/10)

    return c

if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        x = int(input())
        n = x%10
        count = 0

        for j in range(1,n):
            count = count + 10
        
        num_digits = numberDigits(x)

        for k in range(1,num_digits+1):
            count = count + k

        print(count) 