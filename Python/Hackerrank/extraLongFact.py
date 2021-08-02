# Question Link: https://www.hackerrank.com/challenges/extra-long-factorials/problem
def extraLongFactorials(num):
    if num == 1:
        return 1
    else:
        return num*extraLongFactorials(num-1)

if __name__ == "__main__":
    n = int(input())
    res = extraLongFactorials(n)

    print(res)