def subsets(arr):
    res = []
    subsets = []

    def dfs(i):
        if i>=len(arr):
            res.append(subsets.copy())
            return

        subsets.append(arr[i])
        dfs(i+1)

        subsets.pop()
        dfs(i+1)

    dfs(0)

    return res