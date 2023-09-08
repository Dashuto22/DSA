def find_disappear_num(nums):

    for n in nums:
        i = abs(n) -1
        nums[i] = -1 * abs(nums[i])

    res = []

    for i,n in enumerate(nums):
        if nums[i] >0:
            res.append(i+1)

    return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    val = find_disappear_num(nums)
    print(val)