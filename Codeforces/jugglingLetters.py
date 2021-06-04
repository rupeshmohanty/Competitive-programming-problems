if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n = int(input())
        res = ""
        (temp,count) = ([],0)

        for k in range(n):
            s = input()
            res += s
        
        for j in res:
            if(j not in temp):
                if(res.count(j) % n == 0):
                    temp.append(j)
                else:
                    count += 1
            
        if(count > 0):
            print("NO")
        else:
            print("YES")