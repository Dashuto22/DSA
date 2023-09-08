def permutations(arr):
    res = []

    if len(arr) == 1:
        res.append(arr[:])
    for i in range(len(arr)):
        n = arr.pop(0)
        perms = permutations(arr)
        for perm in perms:
            perm.append(n)
        res.extend(perms)

        arr.append(n)

    return res



if __name__ == '__main__':
    nums = [1, 2, 3]
    val = permutations(nums)
    print(val)