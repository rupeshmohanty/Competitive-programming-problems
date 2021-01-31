def restrictTuple(l,K):
    final = []
    m = dict()

    for sub in l:
        if sub[0] not in m.keys():
            m[sub[0]] = 1
        else:
            m[sub[0]] += 1

        if m[sub[0]] <= K:
            final.append(sub)

    return final


if __name__ == '__main__':
    arr = list(input().split())
    k = int(input())
    res = restrictTuple(arr,k)
    print(res)
