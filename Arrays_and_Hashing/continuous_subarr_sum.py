def continuous_subarr_sum(nums, k):
    remMap = {0:-1}
    total = 0
    for i in range(len(nums)):
        total +=nums[i]
        rem = total % k
        if rem not in remMap:
            remMap[rem] = i

        elif i- remMap[rem]>1:
            return True

    return False



if __name__ == '__main__':
    nums = [23, 2, 4, 6, 7]
    k = 6
    val = continuous_subarr_sum(nums,k)
    print(val)