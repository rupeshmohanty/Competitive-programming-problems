def maxSum(arr,n):
    m = min(arr)
    m1 = 0

    for i in range(n):
        m1 += arr[i]
        if m < m1:
            m = m1
        
        if m1 < 0:
            m1 = 0
    
    return m

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    res = maxSum(a, n)
    print(res)