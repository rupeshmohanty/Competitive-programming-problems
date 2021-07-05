if __name__ == "__main__":
    n = int(input())
    card = list(map(int,input().split()))
    (s,d) = (0,0)

    for i in range(n):
        if i % 2 == 0:
            s += max(card)
            card.remove(max(card))
        else:
            d += max(card)
            card.remove(max(card))
    
    print(s,d)