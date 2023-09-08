def optimal_partition(s):
    curset = set()
    res = 1
    for c in s:
        if c in curset:
            res +=1
            curset = set()
        curset.add(c)

    return res


if __name__ == '__main__':
    s = "abacaba"
    val = optimal_partition(s)
    print(val)