if __name__ == "__main__":
    n = int(input())
    a = [0,1]
    temp = 0

    for i in range(2,n):
        temp = a[i-1] + a[i-2]
        a.append(temp)

    print(a)