def reverseArray(arr):
    return arr[::-1]

if __name__ == "__main__":
    a = list(map(int,input().split()))

    res = reverseArray(a)
    print(res)