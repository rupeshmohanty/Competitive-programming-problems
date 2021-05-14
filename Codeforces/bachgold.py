if __name__ == "__main__":
    n = int(input())
    count = 0
    r = [2,3]
    temp = []

    if(n % 2 == 0):
        for i in range(n):
            count = count + 2
            temp.append(2)

            if(count == n):
                break

    else:
        if(n > 3):
            for i in range(n):
                count = count + 2
                temp.append(2)

                if(n - count == 3):
                    count = count + 3
                    temp.append(3)
                    break
        else:
            count = 1
            temp.append(n)
        
    print(len(temp))
    st = ' '.join(str(e) for e in temp)
    print(st)