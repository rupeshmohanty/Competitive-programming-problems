if __name__ == "__main__":
    n = int(input())
    count = 0

    for i in range(1,n):
        temp = n
        temp = temp - i
        if(temp % i == 0):
            count += 1
        

    print(count)