if __name__ == "__main__":
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    temp = []

    for i in range(1,d+1):
        if(i % k == 0):
            temp.append(i)
        elif(i % l == 0):
            temp.append(i)
        elif(i % m == 0):
            temp.append(i)
        elif(i % n == 0):
            temp.append(i)
        else:
            continue
    
    print(len(temp))