def maxMin(arr):
    return (max(arr),min(arr))

if __name__ == "__main__":
    a = list(map(int, input().split()))
    (r1,r2) = maxMin(a)

    print(r1,r2)