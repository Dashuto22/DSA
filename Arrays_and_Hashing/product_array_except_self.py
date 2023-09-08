def product_arr_except_self(nums):
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix *= nums[i]

    return res



if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    val = product_arr_except_self(nums)
    print(val)