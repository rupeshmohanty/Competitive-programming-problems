for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    c = 0
    for i in range(1, n):
        a = max(arr[i], arr[i-1])
        b = min(arr[i], arr[i-1])
        while a > 2 * b:
            b *= 2                   
            c += 1
    print(c)