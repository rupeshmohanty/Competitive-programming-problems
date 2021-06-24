if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        count = 0

        if(n <= 3):
            count = n - 1
        else:
            if(n % 2 == 0):
                count = 2
            else:
                count = 3
        
        print(count)
