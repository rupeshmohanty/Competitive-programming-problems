lines = []

while True:
    s = input()
    
    if s:
        lines.append(s.upper())
    else:
        break

for i in lines:
    print(i)