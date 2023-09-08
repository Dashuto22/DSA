def longest_common_seq(arr):
    numset = set(arr)
    longest = 0
    for n in arr:
        if (n-1) not in numset:
            length = 0
            while (n+ length) in numset:
                length +=1
            longest = max(longest, length)

    return longest


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    val =  longest_common_seq(nums)
    print(val)