def Palindrome(arr):
    r = arr[::-1]

    if(arr == r):
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    l = input()
    res = Palindrome(l)
    print(res)