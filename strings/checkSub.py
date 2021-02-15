def checkSub(s1,s2):
    if(s2.find(s1) == -1):
        return "No"
    else:
        return "Yes"

if __name__ == "__main__":
    sub1 = input()
    sub2 = input()

    res = checkSub(sub1,sub2)
    print(res)