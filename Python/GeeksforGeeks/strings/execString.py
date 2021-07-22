def execString(st):
    r = exec(st)

    return r


if __name__ == "__main__":
    s = """
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact
        
print(factorial(5))
"""
        
    res = execString(s)
    print(res)