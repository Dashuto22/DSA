def first_missing_positive(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i] = 0

    for i in range(len(arr)):
        val = abs(arr[i])
        if 1<=val<=len(arr):
            if arr[val-1] > 0:
                arr[val-1] *= -1
            elif arr[val-1] == 0:
                arr[val-1] = -1 * (len(arr) +1)

    for i in range(1,len(arr)+1):
        if arr[i-1]>=0:
            return i
    return len(arr)+1


if __name__ == '__main__':
    nums = [1, 2, 0]
    val = first_missing_positive(nums)
    print(val)