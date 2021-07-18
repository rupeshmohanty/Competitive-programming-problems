def findNext(l,i,j,K):
    for a in range(i,len(l)):
        for j in range(j,len(l[i])):
            if(l[i][j] == K):
                return (i,j)

if __name__ == '__main__':
    arr = [[4, 3, 1, 2, 3], [7, 5, 3, 6, 3], [8, 5, 3, 5, 3], [1, 2, 3, 4, 6]]
    x = int(input())
    y = int(input())
    k = int(input())

    res = findNext(arr,x,y,k)
    print(res)
