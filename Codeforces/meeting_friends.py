if __name__ == "__main__":
    a = list(map(int,input().split()))
    a.sort()
    dist = 0

    dist = dist + abs(a[0] - a[1]) + abs(a[2] - a[1])
    print(dist)