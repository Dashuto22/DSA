from functools import cmp_to_key


def largest_num(nums):
    for i in range(len(nums)):
        nums[i] = str(nums[i])

    def compare(n1, n2):
        if n1+n2 > n2+n1:
            return -1
        else:
            return 1

    nums = sorted(nums, key = cmp_to_key(compare))

    return str(int("".join(nums)))

if __name__ == '__main__':
    nums = [10,2]
    val = largest_num(nums)
    print(val)