def sqMatrix(A):
    res = []

    for i in range(len(A)):
        temp = []
        for j in range(len(A[i])-1):
            if A[i][j] == 1 and A[i][j+1] == 1:
                temp.append([A[i][j],A[i][j+1]])
            else:
                temp = []
        res.append(temp)
    
    return res


if __name__ == "__main__":
    A = [[1,0,0,1,0], [1,1,1,1,1],[1,0,1,1,1], [0,0,1,1,0] , [1,1,1,1,1]]
    res = sqMatrix(A)
    print(res)