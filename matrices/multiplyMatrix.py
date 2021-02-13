def multiplyMatrix(x,y):
    r = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                r[i][j] += x[i][k] * y[k][j]

    return r
if __name__ == "__main__":
    A = [[12,7,3], 
    [4,5,6], 
    [7,8,9]] 
  
    B = [[5,8,1,2], 
        [6,7,3,0], 
        [4,5,9,1]]

    res = multiplyMatrix(A,B)
    print(res) 