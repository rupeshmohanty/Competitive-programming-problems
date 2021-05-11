if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        count = 0

        # sorting the arrays!
        a.sort()
        b.sort()

        for i in range(n):
            if(a[i] != a[0] or b[i] != b[0]):
                if(abs(a[i] - a[0]) > abs(b[i] - b[0])):
                    count = count + abs(a[i] - a[0])
                else:
                    count = count + abs(b[i] - b[0])

        print(count)