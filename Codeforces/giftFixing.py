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

        for i in range(1,n):
            count = count + max((a[i] - a[0]),(b[i] - b[0]))
        
        print(count)