def combination_sum(candidates, target):
    res = []
    def helper(i, cur, total):
        if i>=len(candidates) or total >target:
            return
        if total == target:
            res.append(cur.copy())
            return

        cur.append(candidates[i])
        helper(i,cur, total+ candidates[i])

        cur.pop()
        helper(i+1, cur, total)
    helper(0,[], 0)

    return res


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    val = combination_sum(candidates, target)
    print(val)