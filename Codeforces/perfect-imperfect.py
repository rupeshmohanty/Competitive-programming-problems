import math

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        prod = 1
        x = 0

        for i in range(n):
            prod *= arr[i]

        x = int(math.sqrt(prod))

        if(pow(x,2) == prod):
            print("NO")
        else:
            print("YES")