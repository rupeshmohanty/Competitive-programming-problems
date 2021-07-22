if __name__ == "__main__":
    a, b = map(int, input().split())
    count = 0

    i = 0
    while(i >= 0):
        a = a*3
        b = b*2

        if(a > b):
            count = count + 1
            break
        else:
            count = count + 1
        i = i + 1
    
    print(count)