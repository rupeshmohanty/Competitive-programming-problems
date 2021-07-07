def kSmall(arr,n,k):
    arr.sort()

    return arr[k-1]

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    res = kSmall(a, n, k)
    print(res)