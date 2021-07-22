if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        num = int(input())
        count = 0

        if(num % 2 == 0):
            count = count + num/2 - 1
        else:
            count = count + int(num/2)
    
        print(int(count))