from itertools import permutations

def formstring(st):
    l = permutations(st)
    
    for i in list(l):
        print(''.join(i))

if __name__ == "__main__":
    s = input()
    res = formstring(s)
    print(res)