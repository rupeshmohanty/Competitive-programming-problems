def checkVowel(st):
    vowel = ['a','e','i','o','u']
    st = st.lower()
    
    for sub in vowel:
        if sub not in st:
            return "Not Accepted"
    
    return "Accepted"

if __name__ == "__main__":
    s = input()
    res = checkVowel(s)
    print(res)