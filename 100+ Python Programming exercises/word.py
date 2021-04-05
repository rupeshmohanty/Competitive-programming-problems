if __name__ == "__main__":
    s = input()
    (u,l) = (0,0)

    for c in s:
        if(c.isupper()):
            u = u + 1
        else:
            l = l + 1
    
    if(u > l):
        s = s.upper()
    else:
        s = s.lower()

    print(s)