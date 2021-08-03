# Question Link: https://practice.geeksforgeeks.org/problems/a512e4b2e812b6df2159b19cc7090ffc1ab056dd/1/?page=1&query=page1#
def maxSubarrayXOR(N,arr):
    m = arr[0]
    s = 0

    for i in range(N):
        s = s^arr[i]

        if s > m:
            m = s
        else:
            s = 0
    
    return m

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    print(maxSubarrayXOR(n,arr))