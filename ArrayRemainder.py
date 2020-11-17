def ArrayRemainder(arr,n):
    prod = 1
    for i in range(len(arr)):
        prod = prod*arr[i]
    res = prod % n
    print(res)

if __name__ == "__main__":
    a = list(map(int,input().strip().split()))
    no = int(input())
    ArrayRemainder(a,no)