def pivot_index(nums):
    total = sum(nums)
    leftSum = 0

    for i,n in enumerate(nums):
        rightSum = total-nums[i]-leftSum
        if rightSum == leftSum:
            return i
        leftSum += n

    return -1


if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    val = pivot_index(nums)
    print(val)