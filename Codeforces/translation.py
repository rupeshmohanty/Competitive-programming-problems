if __name__ == "__main__":
    s = input()
    t = input()
    count = 0
    
    t = t[::-1]
    if(s == t):
        print("YES")
    else:
        print("NO")