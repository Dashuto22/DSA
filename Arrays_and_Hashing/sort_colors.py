def sort_colors(arr):
    l,r = 0, len(arr)-1
    i = 0

    def swap(x,y):
        arr[x], arr[y] = arr[y], arr[x]

    while i <=r:
        if arr[i] == 0:
             swap(l,i)
             l +=1

        elif arr[i] == 2:
            swap(i,r)
            r -= 1
            i -= 1
        i += 1

    return


if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    val = sort_colors(nums)
    print(val)