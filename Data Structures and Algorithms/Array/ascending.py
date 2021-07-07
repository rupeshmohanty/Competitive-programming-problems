def ascending(arr):
    arr.sort()

    return arr

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    res = ascending(arr)
    print(" ".join(str(e) for e in res))