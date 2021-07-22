# Accenture previous year questions!
def MaxInArray(a,n):
    m = max(a)

    for i in range(n):
        if a[i] == m:
            return (m,i)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    n = len(arr)
    res = MaxInArray(arr, n)
    print(res[0])
    print(res[1])