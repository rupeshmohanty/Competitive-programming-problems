s = input()
l = len(s)
player1,player2 = 0,0

for i in range(l):
    if s[i] in "AEIOU":
        player1 += l - i
    else:
        player2 += l - i

if player1 > player2:
    print("Kevin",player1)
elif player2 > player1:
    print("Stuart",player2)
else:
    print("Draw")