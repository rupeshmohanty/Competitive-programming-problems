if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        b = bin(n).replace('0b',"")
        p = len(b) - 1
        print((2**p) - 1)