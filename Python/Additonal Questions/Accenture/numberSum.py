def NumberSum(a,n):
    a.sort()

    return a[0] + a[n - 1]

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    res = NumberSum(arr, n)
    print(res)