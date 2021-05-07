def addSubtract(a,b):
    add = [[0,0],
    [0,0]]

    sub = [[0,0],
    [0,0]]

    for i in range(len(a)):
        for j in range(len(a[0])):
            add[i][j] = a[i][j] + b[i][j]
            sub[i][j] = a[i][j] - b[i][j]
    
    return (add,sub)

if __name__ == "__main__":
    X = [[1,2],[3,4]]
    Y = [[4,5],[6,7]]

    (add,sub) = addSubtract(X,Y)
    print(add)
    print(sub)