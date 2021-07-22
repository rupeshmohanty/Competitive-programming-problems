if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        h,m = map(int,input().split())
        totalMinutes = 1440

        minutes = 1440 - ((h*60) + m)
        print(minutes)