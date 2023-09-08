def num_zero_filled_subarr(nums):
    res,i = 0,0
    while i < len(nums):
        count =0
        while i < len(nums) and nums[i]==0:

            count +=1
            res += count
            i +=1
        i +=1
    return res


if __name__ == '__main__':
    nums = [1, 3, 0, 0, 2, 0, 0, 4]
    val = num_zero_filled_subarr(nums)
    print(val)