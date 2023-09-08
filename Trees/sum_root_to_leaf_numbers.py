class TreeNode:
    def __init__(self, val = 0, left=None, right =None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sum_root_to_leaf(self,root):
        def dfs(cur, num):
            if not cur:
                return 0
            num = num *10 + cur.val

            if not cur.left and not cur.right:
                return num
            return dfs(cur.left, num) + dfs(cur.right, num)

        return dfs(root, 0)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    sol = Solution()

    val = sol.sum_root_to_leaf(root)

    print(val)