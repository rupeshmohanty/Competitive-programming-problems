if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    diff_sum = 0

    arr.sort()

    for i in range(n-1):
        if(i % 2 == 0):
            diff_sum += abs(arr[i] - arr[i+1])

    print(diff_sum)