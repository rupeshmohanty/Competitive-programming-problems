haystack = input()
needle = input()

if needle in haystack:
    print(haystack.find(needle))
else:
    print(-1)