class Solution:
    def numTrees(self,n):
        numTrees = [1] *(n+1)

        for nodes in range(2, n+1):
            total = 0
            for root in range(1, nodes+1):
                left = root-1
                right = nodes -root
                total += numTrees[left] * numTrees[right]
            numTrees[nodes] = total

        return numTrees[n]


if __name__ == '__main__':
    n = 3
    sol = Solution()
    res =  sol.numTrees(3)

    print(res)