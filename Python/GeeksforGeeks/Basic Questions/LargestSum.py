def LargestNum(arr):
    n = len(arr)
    arr.sort()
    return arr[n-1]

if __name__ == "__main__":
    a = list(map(int,input().strip().split()))
    res = LargestNum(a)
    print(res)
            