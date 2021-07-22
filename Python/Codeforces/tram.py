if __name__ == "__main__":
    n = int(input())
    (sum,min) = (0,0)

    for i in range(n):
        t1 = []
        t1 = list(map(int,input().split()))

        sum = sum - t1[0]
        sum = sum + t1[1]

        if(sum > min):
            min = sum

    print(min)