if __name__ == "__main__":
    r,c = map(int,input().split())
    count = 0
    r1 = []
    c1 = []

    for j in range(r):
        s = input()

        for i in range(c):
            if s[i] == 'S':
                c1.append(i)
                r1.append(j)
                count += 1
    
    if(count == r*c):
        print(0)
    else:
        print(r*c - len(set(r1))*len(set(c1)))