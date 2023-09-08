def partition(nums,l,r):
    pivot, fill = nums[r], l

    for i in range(l,r):
        if nums[i] <=pivot:
            nums[fill], nums[i] = nums[i], nums[fill]
            fill += 1

    nums[fill], nums[r] = nums[r], nums[fill]

    return fill

def kth_largest(nums, k):

    k = len(nums)-k
    l, r = 0, len(nums)-1
    while l < r:
        pivot = partition(nums, l,r)

        if pivot <k:
            l = pivot + 1
        elif pivot > k:
            r = pivot - 1
        else:
            break
    return nums[k]

if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    val = kth_largest(nums, k)
    print(val)