class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isValidBST(self, root):

        def dfs(node, left, right):
            if not node:
                return True

            if not(node.val < right and node.val >left):
                return False

            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float("-inf"), float("inf"))

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.right = TreeNode(6)
    root.right.left = TreeNode(3)

    sol = Solution()

    res = sol.isValidBST(root)

    print(res)
