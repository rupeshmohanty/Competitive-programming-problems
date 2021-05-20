if __name__ == "__main__":
    t = int(input())
    
    for i in range(t):
        n = int(input())
        s = input()
        last = n-1
        count = 0

        if(n < 3):
            print("YES")
        else:
            for i in range(len(s)):
                if(s.count(s[i]) != n):
                    if(i != last):
                        if(s[i] == s[last]):
                            count = count + 1
                    last -= 1
            
            if(count == 0):
                print("YES")
            else:
                print("NO")