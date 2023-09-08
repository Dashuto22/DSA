def majority_ele(arr):
    count, res = 0, 0
    for n in arr:
        if count ==0:
            res = n
        count += (1 if res==n else -1)

    return res

if __name__ == '__main__':
    arr = [2,2,1,3,2,2]
    val =  majority_ele(arr)
    print(val)