if __name__ == "__main__":
    n = int(input())
    count = 0
    arr = []

    for i in range(n):
        s = input()
        st = list(s)

        if(count == 0):
            for i in range(len(st)-1):
                if(st[i] == 'O' and st[i+1] == 'O'):
                    count += 1
                    (st[i],st[i+1]) = ('+','+')
                    break  
                else:
                    continue
        arr.append("".join(str(e) for e in st))

    if(count == 1):
        print("YES")
        for i in range(len(arr)):
            print(arr[i])
    else:
        print("NO")
