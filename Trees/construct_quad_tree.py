class TreeNode:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct_quad_tree(self, grid):

        def dfs(n, r,c):
            allSame = True

            for i in range(n):
                for j in range(n):
                    if grid[i][j]!= grid[r+i][c+j]:
                        allSame = False
                        break
            if allSame:
                return TreeNode(grid[r][c], True, None, None, None, None)

            n = n//2

            topLeft =  dfs(n,r,c)
            topRight = dfs(n,r, c+n)
            bottomLeft = dfs(n,r+n,c)
            bottomRight = dfs(n,r+n, c+n)


            return TreeNode(0, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid),0,0)

if __name__ == '__main__':
    grid = [[0,1], [1,0]]
    solution = Solution()
    res = solution.construct_quad_tree(grid)

    print(res)