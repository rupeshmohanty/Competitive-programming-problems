def matrixProd(a):
    prod = 1

    for i in range(len(a)):
        for j in range(len(a[i])):
            prod *= a[i][j]

    return prod

if __name__ == "__main__":
    x = [[1,4,5],[7,3],[4],[46,7,3]]
    res = matrixProd(x)
    print(res)