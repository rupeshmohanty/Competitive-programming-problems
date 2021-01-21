def SwapPos(l,p,q):
    temp = 0

    temp = l[p]
    l[p] = l[q]
    l[q] = temp

    return l

if __name__ == "__main__":
    arr = list(map(int,input().strip().split()))
    pos1 = int(input())
    pos2 = int(input())
    res = SwapPos(arr,pos1,pos2)
    print(res)