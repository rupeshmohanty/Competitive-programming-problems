if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        s = input()
        test_str = []
        res = ""
        
        res = res + s[0] + s[1]
        
        for k in range(3,len(s),2):
            res = res + s[k]

        print(res)

        

        