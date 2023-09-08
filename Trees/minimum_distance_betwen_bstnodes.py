class TreeNode:
    def __init__(self, val= 0,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffbst(self, root):
        prev, res = None, float("inf")

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal  prev,res
            if prev:
                res = min(res, node.val-prev.val)
            prev = node
            dfs(node.right)

        dfs(root)

        return res

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)

    root.left.right = TreeNode(3)
    root.left.left = TreeNode(1)

    solution =  Solution()

    res = solution.minDiffbst(root)

    print(res)