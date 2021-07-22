if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        s = input()
        res = []
        c = 0

        if(s.count('1') == 0):
            print(0)
        else:
            for i in range(len(s)):
                if(s[i] == '1'):
                    res.append(i)
            
            for j in range(len(res)-1):
                if(res[j+1] - res[j] > 1):
                    c += res[j+1] - res[j] - 1
            
            if(c > 0):
                print(c)
            else:
                print(c)