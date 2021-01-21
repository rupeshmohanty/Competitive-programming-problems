def secondLargest(l):
    l.sort()
    return l[len(l)-2]

if __name__ == '__main__':
    arr = list(map(int,input().split()))

    res = secondLargest(arr)
    print(res)