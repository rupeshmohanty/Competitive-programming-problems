if __name__ == "__main__":
    s1 = input()
    s2 = input()
    s3 = input()
    term = 0

    s = s1+s2

    if(sorted(s) == sorted(s3)):
        print("YES")
    else:
        print("NO")
    