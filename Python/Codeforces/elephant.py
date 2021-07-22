def countSteps(X):
    count = 0
    l = [1,2,3,4,5]
    n = len(l)

    while(X > l[n-1]):
        X = X - l[n-1]
        count = count + 1
    
    if X in l:
        count = count + 1

    return count


if __name__ == "__main__":
    x = int(input())
    res = countSteps(x)
    print(res)