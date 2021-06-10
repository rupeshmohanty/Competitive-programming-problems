if __name__ == "__main__":
    n = int(input())
    s = input()
    (max,min) = (0,0)

    max += s.count("R")
    min -= s.count("L")

    diff = max - min
    print(diff+1)
