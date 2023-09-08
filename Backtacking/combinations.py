def combinations(n,k):
    res = []
    comb = []
    def backtrack(start):
        if len(comb) ==k:
            res.append(comb.copy())
            return
        for i in range(start, n+1):
            comb.append(i)
            backtrack(i+1)
            comb.pop()

    backtrack(1)
    return res

if __name__ == '__main__':
    n = 4
    k = 2
    val = combinations(n,k)
    print(val)