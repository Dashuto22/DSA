def next_greater_ele(nums1, nums2):

    num1map ={n:i for i,n in enumerate(nums1)}

    res =[-1] * len(nums1)
    st = []

    for i in range(len(nums2)):
        cur = nums2[i]
        while st and cur > st[-1]:
            val = st.pop()
            idx = num1map[val]
            res[idx] = cur
        if cur in num1map:
            st.append(cur)

    return res



if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    val = next_greater_ele(nums1, nums2)
    print(val)