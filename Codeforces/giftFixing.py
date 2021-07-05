if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        ma = min(a)
        mb = min(b)
        ans = 0

        for i in range(n):
            ans += max(a[i] - ma, b[i] - mb)
        
        print(ans)