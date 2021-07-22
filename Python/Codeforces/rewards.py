import math

if __name__ == "__main__":
    (a1,a2,a3) = map(int,input().split())
    (b1,b2,b3) = map(int,input().split())
    n = int(input())

    cups = a1 + a2 + a3
    medals = b1 + b2 + b3
    count = 0

    count += math.ceil(cups/5) + math.ceil(medals/10)
    
    if(count <= n):
        print("YES")
    else:
        print("NO")

