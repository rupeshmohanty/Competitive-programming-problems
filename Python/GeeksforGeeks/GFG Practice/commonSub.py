# Question Link: https://practice.geeksforgeeks.org/problems/common-subsequence-oldp3752/1/?category[]=Strings&category[]=Strings&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]StringsproblemStatusunsolveddifficulty[]0page1category[]Strings
def compareElements(s1,s2):
    for ele in s1:
        if ele in s2:
            return 1
            
    return 0

if __name__ == "__main__":
    s1 = input()
    s2 = input()    

    print(compareElements(s1,s2))