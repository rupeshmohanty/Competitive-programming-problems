import math

def squareRoot(st,C,H):
    r = []
    temp = 0

    for i in range(len(st)):
        temp = round(math.sqrt((2*C*int(st[i]))/H))
        r.append(temp)

    return r

if __name__ == "__main__":
    s = input().split(',')
    c = 50
    h = 30
    res = squareRoot(s,c,h)
    print(res)
