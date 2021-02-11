if __name__ == '__main__':
    arr = [[1,3,"gfg"],[2,"is",4],["best",9,5]]
    in_del = input()
    out_del = input()

    res = out_del.join([in_del.join([str(ele) for ele in sub]) for sub in arr])
    print(res)
