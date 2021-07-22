if __name__ == "__main__":
    n, k, l, c, d, p, nl, np = map(int,input().split())
    
    drink = int((k*l)/nl)
    lime = c*d
    salt = int(p/np)

    print(int(min(drink,lime,salt)/n))