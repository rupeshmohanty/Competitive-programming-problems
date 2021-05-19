if __name__ == "__main__":
    s = input()
    c = input()
    count = 0

    for i in s:
        if(c.find(i) != -1):
            count = count + 1
        
    if(count > 0):
        print("YES")
    else:
        print("NO")