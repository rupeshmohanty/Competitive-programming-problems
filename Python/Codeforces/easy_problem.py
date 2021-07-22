if __name__ == "__main__":
    n = int(input())
    l = list(map(int,input().split()))

    # easy and hard questions count!
    easy = 0
    hard = 0

    for i in range(len(l)):
        if(l[i] == 0):
            easy = easy + 1
        else:
            hard = hard + 1
        
    if(easy == len(l)):
        print("EASY")
    else:
        print("HARD")