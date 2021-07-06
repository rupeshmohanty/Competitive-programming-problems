# Accenture previous year questions!
def CheckPassword(s,n):
    check = 0

    # check number of characters!
    if n >= 4:
        check = 1
    else:
        check = 0
    
    # checking for first element!
    if s[0] >= '0' and s[0] <= '9':
        check = 0
    else:
        check = 1

    # other checkings
    for i in range(n):
        if s[i] >= '0' and s[i] <= '9':
            check = 1
        elif s[i] >= 'A' and s[i] <= 'Z':
            check = 1
        elif s[i] == '/' or s[i] == ' ':
            check = 0
        else:
            check = 0
    
    return check

if __name__ == "__main__":
    s = input()
    n = len(s)
    res = CheckPassword(s, n)
    print(res)
    
