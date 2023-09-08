
#unstable
#TC->O(n**2)
def quick_sort(arr,s,e):
    if e-s+1<=1:
        return

    pivot = arr[e]
    left = s

    for i in range(s,e):
        if pivot >= arr[i]:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    arr[e] = arr[left]
    arr[left]= pivot

    quick_sort(arr,s, left-1)
    quick_sort(arr, left+1, e)

    return arr


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    val = quick_sort(arr,0, len(arr)-1)
    print(val)