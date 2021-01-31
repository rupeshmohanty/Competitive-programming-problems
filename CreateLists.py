import random

def splitLists(l,K,N):
    m = []
    tempList = []
    for i in range(N):
        tempList = [] # making the temporary list empty
        for j in range(K):
            temp = random.choice(l)
            tempList.append(temp)
        if(tempList not in m):
            m.append(tempList)
    return m

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    k = int(input())
    n = int(input())
    res = splitLists(arr,k,n)
    print(res)
