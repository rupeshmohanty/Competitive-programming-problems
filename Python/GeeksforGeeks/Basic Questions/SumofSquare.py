def SumofSquare(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i*i
    return sum

if __name__ == "__main__":
    num = int(input())
    res = SumofSquare(num)
    print(res) 