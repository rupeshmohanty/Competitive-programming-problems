if __name__ == "__main__":
    a = list(map(int,input().split()))
    s = input()
    sum = 0

    for i in range(len(s)):
        sum += a[int(s[i])-1]
    
    print(sum)