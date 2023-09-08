
#stable
#T.C.->O(nlogn)
def merge_sort(arr):

    def merge(arr, L,M,R):
        left, right = arr[L:M+1], arr[M+1: R+1]
        i,j,k = L,0,0
        while j < len(left) and k <len(right):
            if left[j] <=right[k]:
                arr[i] = left[j]
                i +=1
                j +=1

            else:
                arr[i] = right[k]
                i += 1
                k += 1

        while j < len(left):
            arr[i] = left[j]
            i +=1
            j +=1

        while k < len(right):
            arr[i] =right[k]
            i +=1
            k +=1


    def split_array(arr,l,r):
        if l==r:
            return arr
        mid = l+ (r-l)//2
        split_array(arr, l, mid)
        split_array(arr, mid+1, r)
        merge(arr,l,mid,r)

    return split_array(arr, 0, len(arr)-1)


if __name__ == '__main__':
    arr = [5,3,2,1]
    val = merge_sort(arr)
    print(val)