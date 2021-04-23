def subtractions(num1,num2):
    if(num1 % 10 == 0):
        num1 = num1/10
        num2 = num2 - 1
    else:
        num1 = num1 - 1
        num2 = num2 - 1
    
    if(num2 == 0):
        return int(num1)
    else:
        return subtractions(num1,num2)

if __name__ == "__main__":
    n1 = int(input())
    n2 = int(input())
    res = subtractions(n1,n2)
    print(res)