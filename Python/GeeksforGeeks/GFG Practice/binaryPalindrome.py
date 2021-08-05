# Question Link: https://practice.geeksforgeeks.org/problems/check-if-actual-binary-representation-of-a-number-is-palindrome0624/1/?category[]=Strings&category[]=Strings&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]StringsproblemStatusunsolveddifficulty[]0page1category[]Strings
if __name__ == "__main__":
    n = int(input())
    s = bin(n).replace("0b", "")

    t = str(s)

    if t == t[::-1]:
        print(1)
    else:
        print(0)
