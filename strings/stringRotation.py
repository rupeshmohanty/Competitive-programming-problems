def stringRotation(st,k):
    sr = ""
    sl = ""
    # for left rotation
    for i in range(k,len(st)):
        sl = sl + st[i]
    
    for i in range(k):
        sl = sl + st[i]

    #  for right rotation
    for i in range(len(st)-k,len(st)):
        sr = sr + st[i]
    
    for i in range(len(st)-k):
        sr = sr + st[i]

    return (sl,sr)

if __name__ == "__main__":
    s = input()
    d = int(input())
    (res1,res2) = stringRotation(s,d)
    print("Left Rotation: ",res1)
    print("Right Rotation: ",res2)