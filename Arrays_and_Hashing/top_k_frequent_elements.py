def top_k_frequent(nums, k):
    countMap = {}
    freq =[[] for i in range(len(nums)+1)]

    for i in range(len(nums)):
        countMap[nums[i]] = 1 + countMap.get(nums[i], 0)

    for c,n in countMap.items():
        freq[c].append(n)

    res = []

    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res



if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    val = top_k_frequent(nums, k)
    print(val)