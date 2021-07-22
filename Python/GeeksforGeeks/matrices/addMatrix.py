def addMatrix(a,b):
    r = [[0,0,0],
    [0,0,0],
    [0,0,0]]

    for i in range(len(a)):
        for j in range(len(a[0])):
            r[i][j] = a[i][j] + b[i][j]
    
    return r

if __name__ == "__main__":
    X = [[1,2,3],[4,5,6],[7,8,9]]
    Y = [[9,8,7],[6,5,4],[3,2,1]]

    res = addMatrix(X,Y)
    print(res)