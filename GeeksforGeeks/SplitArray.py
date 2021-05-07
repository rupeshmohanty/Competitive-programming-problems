def SplitArray(arr,d):
    temp = []
    a = []
    n = len(arr)
    for i in range(d):
        temp.append(arr[i])
    
    for i in range(d,n):
        a.append(arr[i])
    res = a + temp
    print(res)

if __name__ == "__main__":
    arr = list(map(int,input().strip().split()))
    d = int(input())
    SplitArray(arr,d)      

    