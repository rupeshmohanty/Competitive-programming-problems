if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    maxm = 0

    for i in range(1,n):
        if arr[i] > arr[i-1]:
            count += 1
            if count > maxm:
                maxm = count
        else:
            count = 0

    print(maxm+1)