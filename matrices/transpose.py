def transpose(x):
    a = []
    b = []
    res = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            if(j+1 < len(x[i])):
                a.append(x[i][j])
                b.append(x[i][j+1])
    
    res.append(a)
    res.append(b)

    return res

if __name__ == "__main__":
    X = [[1,2],[3,4],[5,6]]
    res = transpose(X)
    print(res)