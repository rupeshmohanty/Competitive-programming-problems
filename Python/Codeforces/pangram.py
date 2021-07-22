import string

if __name__ == "__main__":
    n = int(input())
    ip = input().lower()
    alpha = list(string.ascii_lowercase)
    count = 0

    for i in alpha:
        if i in ip:
            continue
        else:
            count = count + 1
            break
    
    if(count >= 1):
        print("NO")
    else:
        print("YES")