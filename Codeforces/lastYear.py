if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input()
        res = ""
        two_count = s.count('2')
        zero_count = s.count('0')

        if(s == "2020"):
            print("YES")
        else:
            # check number of 2's and 0's!
            if(two_count < 2 or zero_count < 2):
                print("NO")
            else:
                first = s.find('2')
                second = s.find('020')

                res += s[first]

                for i in range(second,n):
                    res += s[i]
                
                if(res == "2020"):
                    print("YES")
                else:
                    print("NO")