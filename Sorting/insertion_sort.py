
#Stable
#T.C.-> O(nlogn)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        while j>=0 and arr[j]> arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j -= 1

    return arr


if __name__ == '__main__':
    arr = [5,4,3,2,1]
    val = insertion_sort(arr)
    print(val)