def checkBinary(st):
    for i in st:
        if i != '0' and i != '1':
            return "No"
    return "Yes"

if __name__ == "__main__":
    s = input()
    res = checkBinary(s)
    print(res)
    