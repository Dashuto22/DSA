class TreeNode:
    def __int__(self, val =0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathsum(self, root, target):
        def dfs(node, cursum):
            if not node:
                return False

            cursum += node.val

            if not node.left and not node.right:
                return cursum==target

            return (dfs(node.left, cursum) or dfs(node.right, cursum))

        return dfs(root, 0)

