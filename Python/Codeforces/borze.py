if __name__ == "__main__":
    s = input()
    res = ""

    i = 0
    while(i <= len(s)-1):
        if(s[i] == '-'):
            if(s[i+1] == '.'):
                res += "1"
            else:
                res += "2"
            i += 2
        else:
            res += "0"
            i += 1
                

    print(res)