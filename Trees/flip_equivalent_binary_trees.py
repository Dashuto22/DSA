class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flip_equivalent_binary_trees(self, root1, root2):
        if not root1 or not root2:
            return not root1 and not root2

        if root1.val != root2.val:
            return False

        a = self.flip_equivalent_binary_trees(root1.left, root2.left) and self.flip_equivalent_binary_trees(root1.right, root2.right)

        return a or self.flip_equivalent_binary_trees(root1.right, root2.left) and self.flip_equivalent_binary_trees(root1.left, root2.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.left.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)

    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)
    root1.right.right.right = TreeNode(7)
    root1.right.right.left = TreeNode(8)

    root1.left = TreeNode(3)
    root1.left.right = TreeNode(6)

    sol = Solution()

    res = sol.flip_equivalent_binary_trees(root, root1)

    print(res)