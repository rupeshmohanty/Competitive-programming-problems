if __name__ == "__main__":
    n = int(input())
    l = list(map(int,input().split()))
    num = 0

    for i in range(len(l)):
        num = num + l[i]/100
    
    res = (num/len(l))*100
    print(res)
