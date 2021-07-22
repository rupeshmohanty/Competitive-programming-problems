def checkDigit(n):
    if n < 10:
        return True
    else:
        temp = n%10
        temp1 = int(n/10)

        if temp == temp1:
            return True
        else:
            return False

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        count = 0
        flag = False

        if n == 1:
            print(1)
        else:
            for i in range(1,n+1):
                flag = checkDigit(i)
                if flag:
                    count += 1
            
            print(count)