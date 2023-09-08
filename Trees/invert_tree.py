class TreeNode:
    def __init__(self, val = 0, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_binary_tree(self, root):
        if not root:
            return

        tmp = root.left
        root.left = root.right
        root.right = tmp


        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)

        return root

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()

    res = solution.invert_binary_tree(root)

    print(res)