def maximumSum(st):
    sum = 0
    max = 0
    max_word = ""

    for i in st:
        sum = 0 
        for j in i:
            sum = sum + ord(j) - 96
        
        if(sum > max):
            max = sum
            max_word = i

    return max_word

if __name__ == "__main__":
    s = input().split()
    res = maximumSum(s)
    print(res)