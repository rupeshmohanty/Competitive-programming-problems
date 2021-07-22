import random

if __name__ == "__main__":
    t = int(input())
    
    for i in range(t):
        n, m = map(int,input().split())
        arrn = list(map(int,input().split()))
        arrm = list(map(int,input().split()))
        res = []
        count = 0

        if(arrm == arrn):
            count = 1
            res.append(random.choice(arrm))
        else:
            for j in arrm:
                if j in arrn:
                    res.append(j)
                    count += 1
                    if(count == 1):
                        break

        if(count == 0):
            print("NO")
        else:
            print("YES")
            print(count," ".join(str(e) for e in res))