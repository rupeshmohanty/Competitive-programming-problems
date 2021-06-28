if __name__ == "__main__":
    s = input()
    t = input()
    pos = 0
    count = 0

    for i in t:
        if(i == s[pos]):
            pos += 1
            count += 1
    
    print(count+1)
