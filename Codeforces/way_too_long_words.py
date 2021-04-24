if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        s = input()
        string_len = len(s)

        if(string_len > 10):
            print(s[0]+str(string_len-2)+s[string_len-1])
        else:
            print(s)