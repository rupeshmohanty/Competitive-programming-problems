if __name__ == "__main__":
    s = input()
    count = 0

    for i in range(len(s)):
        for j in range(i+1,len(s)):
            for k in range(j+1,len(s)):
                if(s[i] == 'Q' and s[j] == 'A' and s[k] == 'Q'):
                    count += 1
    
    print(count)