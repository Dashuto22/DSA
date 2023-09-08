def subsets2(nums):
    res = []
    subsets = []
    nums.sort()

    def backtrack(i):
        if i == len(nums):
            res.append(subsets.copy())
            return

        subsets.append(nums[i])
        backtrack(i+1)
        subsets.pop()

        while i+1 < len(nums) and nums[i]==nums[i+1]:
            i += 1
        backtrack(i+1)

    backtrack(0)

    return res


if __name__ == '__main__':
    nums = [1, 2, 2]
    val = subsets2(nums)

    print(val)