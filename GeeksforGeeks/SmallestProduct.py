def factors(num):
    factors = []
    res = []
    pair = []
    for i in range(1,num+1):
        if(num % i == 0):
            factors.append(i)

    factors.sort()

    for k in factors:
        if(k>=1 and k<10):
            res.append(k)

    SmallestProduct(num,res)

def SmallestProduct(number,r):
    new = []
    temp = 0
    for j in r:
        if(j != 1):
            temp = int(number/j)
        if(temp >=1 and temp < 10):
            new.append(temp)
        else:
            factors(temp)
    print(new)


if __name__ == "__main__":
    n = int(input())
    factors(n)