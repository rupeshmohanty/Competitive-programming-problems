def distinct(N,K,A):
    temp = {}
    for i in range(N):
        temp[A[i]] = A.count(A[i])

    r = []
    number_count = 0
    for i in range(1,10):
        if(temp[A[i]] == i):
            r.append(A[i])
            number_count += 1         
        if(len(r) == K):
            break
    
    return number_count

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        k = int(input())
        arr = list(map(int,input().split()))
        res = distinct(n,k,arr)
        print(res)