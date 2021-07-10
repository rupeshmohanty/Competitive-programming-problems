def minimizeHeight(arr,k,n):

    for i in range(n):
        if arr[i] > k:
            arr[i] = arr[i] - k
        else:
            arr[i] = arr[i] + k
    
    return max(arr) - min(arr)

if __name__ == "__main__":
    k,n = map(int, input().split())
    a = list(map(int, input().split()))

    res = minimizeHeight(a, k, n)
    print(res)