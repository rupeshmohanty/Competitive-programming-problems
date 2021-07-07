def moveNegative(arr):
    res = []
    pos = []
    for i in range(len(arr)):
        if arr[i] < 0:
            res.append(arr[i])
        else:
            pos.append(arr[i])

    return (res + pos)

if __name__ == "__main__":
    a = list(map(int, input().split()))
    r = moveNegative(a)

    print(" ".join(str(e) for e in r))