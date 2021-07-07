def arrUnion(a,b):
    x = a+b
    return len(set(x))

if __name__ == "__main__":
    n1,n2 = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    res = arrUnion(arr1,arr2)
    print(res)