def combination_sum2(arr, t):
    res = []
    arr.sort()

    def backtrack(pos, cur, total):
        if total == 0:
            res.append(cur.copy())
            return
        if total <=0:
            return

        prev = -1
        for i in range(pos, len(arr)):
            if prev== arr[i]:
                continue
            cur.append(arr[i])
            backtrack(i+1, cur, total- arr[i])
            cur.pop()
            prev = arr[i]

    backtrack(0,[],t)

    return res



if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    val = combination_sum2(candidates, target)
    print(val)
