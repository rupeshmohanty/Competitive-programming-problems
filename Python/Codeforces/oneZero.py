if __name__ == "__main__":
    n = int(input())
    s = input()
    (one,zero) = (0,0)
    res = ""

    one = s.count('n')
    zero = s.count('z')

    res = "1 "*one + "0 "*zero

    print(res)