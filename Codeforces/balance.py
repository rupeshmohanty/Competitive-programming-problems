def balance(N,K,A):
    for i in range(N):
        x = (A[i+1] - A[i])/(K+1)
        if(A[i+1] > A[i]):
            return round(A[i+1] - x,2)
        else:
            return round(A[i] - x,2)

if __name__ == "__main__":
    t = int(input())
    n = int(input())
    k = float(input())
    arr = list(map(int,input().split()))
    res = balance(n,k,arr)
    print(res)