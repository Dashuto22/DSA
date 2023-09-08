def Find_difference(nums1, nums2):
    num1set, num2set = set(nums1), set(nums2)

    res1, res2 = set(), set()

    for n in num1set:
        if n not in num2set:
            res1.add(n)

    for n in num2set:
        if n not in num1set:
            res2.add(n)

    return [list(res1), list(res2)]


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    val = Find_difference(nums1, nums2)
    print(val)