def words(st,K):
    r = []
    for i in st:
        if len(i) > K:
            r.append(i)

    final_string = " ".join(r)
    return final_string


if __name__ == "__main__":
    s = input().split()
    k = int(input())
    res = words(s,k)
    print(res)