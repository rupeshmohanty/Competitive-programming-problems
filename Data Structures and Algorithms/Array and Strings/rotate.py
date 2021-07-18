def arrayRotate(arr,n):
    x = arr[n-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    
    arr[0] = x
    return arr

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    r = arrayRotate(a, n)
    print(" ".join(str(e) for e in r))