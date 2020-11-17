def ArraySum(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    return sum

if __name__ == "__main__":
    a = list(map(int,input().strip().split()))
    res = ArraySum(a)
    print(res)