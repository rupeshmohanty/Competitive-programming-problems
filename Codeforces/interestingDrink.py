if __name__ == "__main__":
    n = int(input())
    x = list(map(int,input().split()))
    x = sorted(x)
    q = int(input())
    c = []

    for i in range(q):
        temp = int(input())
        count = 0
        for j in x:
            if temp >= j:
                count = count + 1
        c.append(count)

    for k in c:
        print(k)
