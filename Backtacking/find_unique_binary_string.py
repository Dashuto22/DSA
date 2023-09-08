def unique_binary_string(nums):
    strset = {s for s in nums}

    def backtrack(i, cur):
        if i==len(nums):
            res = "".join(cur)
            return None if res in strset else res

        res = backtrack(i+1, cur)
        if res:
            return res
        cur[i]= "1"
        res = backtrack(i+1, cur)
        if res:
            return res

    return backtrack(0, ["0" for s in nums])


if __name__ == '__main__':
    nums = ["01", "10"]
    val = unique_binary_string(nums)
    print(val)