
#unstable
#T.C.->O(N)
def bucket_sort(arr):
    arrset = set(arr)
    count = [0] * len(arrset)

    for n in arr:
        count[n] += 1

    i =0
    for n in range(len(count)):
        for j in range(count[n]):
            arr[i] = n
            i +=1
    return arr

if __name__ == '__main__':
    arr = [2,0,1,1,0,1,2]
    val = bucket_sort(arr)
    print(val)