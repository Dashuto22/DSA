def check_possibility(nums):
    changed= False
    for i in range(len(nums)-1):
        if nums[i]<=nums[i+1]:
            continue

        if changed:
            return False

        #3,4,2
        if i==0 or nums[i+1]>=nums[i-1]:
            nums[i]= nums[i+1]
        else:
            nums[i+1]= nums[i]

        changed= True

    return True

if __name__ == '__main__':
    arr = [4,2,3]
    val = check_possibility(arr)
    print(val)