class TreeNode:
    def __init__(self, val =0, left=None, right =None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def issubtree(self, tree, subtree):
        if not subtree:
            return True
        if not tree:
            return False

        if self.isSametree(tree, subtree):
            return True

        return (self.issubtree(tree.left, subtree) or self.issubtree(tree.right, subtree))

    def isSametree(self, t, s):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.isSametree(t.left, s.left) and self.isSametree(t.right, s.right))

        return False


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    root2 = TreeNode(4)
    root2.left = TreeNode(1)
    root2.right = TreeNode(2)

    solution = Solution()
    res = solution.issubtree(root, root2)

    print(res)