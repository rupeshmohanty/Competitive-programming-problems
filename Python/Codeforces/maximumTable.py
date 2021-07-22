def elem(row,col):
    if(row == 1 or col == 1):
        return 1
    else:
        return elem(row-1,col) + elem(row,col-1)

if __name__ == "__main__":
    n = int(input())
    
    res = elem(n,n)
    print(res)