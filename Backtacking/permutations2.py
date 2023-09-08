def permutations2(arr):
    res = []
    perm = []

    count = {n:0 for n in arr}
    for n in arr:
        count[n] += 1

    def backtrack():
        if len(arr)== len(perm):
            res.append(perm[:])
            return
        for n in count:
            if count[n]>0:
                perm.append(n)
                count[n] -=1

                backtrack()

                count[n] +=1
                perm.pop()
    backtrack()
    return res


if __name__ == '__main__':
    arr = [1, 1, 2]
    val = permutations2(arr)
    print(val)