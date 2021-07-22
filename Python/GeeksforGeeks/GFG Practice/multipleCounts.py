def getMaxandMinProduct(A,Q,N,M):
    count = []

    for i in range(M):
        c = 0
        for j in range(N):
            if A[j] % Q[i] == 0:
                c += 1

        count.append(c)

    return count

if __name__ == "__main__":
    N = 6
    A = [2,4,9,15,21,20]
    M = 3
    Q = [2,3,5]
    res = getMaxandMinProduct(A, Q, N, M)
    print(" ".join(str(e) for e in res))