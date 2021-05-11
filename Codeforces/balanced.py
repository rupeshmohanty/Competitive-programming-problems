if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        res = []
        esum = 0
        osum = 0
        r = ""

        if(n % 4 == 0):
            print("YES")
            # Adding even numbers first!
            for j in range(1,int(n/2)+1):
                res.append(2*j)
                esum = esum + 2*j

            # adding odd number next!
            for k in range(1,n):
                if(len(res) != n-1):
                    if(k % 2 != 0):
                        res.append(k)
                        osum = osum + k

            res.append(esum-osum)

            r = ' '.join(str(e) for e in res)
            print(r)
        else:
            print("NO")