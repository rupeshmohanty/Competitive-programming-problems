def alnum(t):
    alcount = 0
    numcount = 0

    for i in t:
        if i.isalpha():
            alcount = alcount + 1
        elif i.isnumeric():
            numcount = numcount + 1
        else:
            continue
    
    if(alcount > 0 and numcount > 0):
        return True
    else:
        return False

if __name__ == "__main__":
    test_str = input()
    res = alnum(test_str)
    print(res)