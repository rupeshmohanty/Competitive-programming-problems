# Program to print numbers with comma between 2000 and 3201 which are divisible by 7 and not a multiple of 5.

def multiple():
    l = []
    r = ""
    for i in range(2000,3201):
        if i%7 == 0 and i%5!= 0:
            l.append(str(i))
    
    r = ','.join(l)
    return r

if __name__ == "__main__":
    res = multiple()
    print(res)