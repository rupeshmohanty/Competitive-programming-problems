# Program to print a dictionary with the pattern (i,i*i) where i is an integral integer.

def squareDict(N):
    dict = {}
    for i in range(1,N):
        dict[i] = i*i
    
    return dict

if __name__ == "__main__":
    n = int(input())
    res = squareDict(n)
    print(res)
