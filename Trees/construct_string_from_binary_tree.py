class TreeNode:
    def __init__(self, val =0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def construct_string(self, root):
        res = []

        def preorder(root):
            if not root:
                return
            res.append("(")
            res.append(str(root.val))
            if not root.left and root.right:
                res.append("()")
            preorder(root.left)
            preorder(root.right)
            res.append(")")
        preorder(root)

        return "".join(res)[1:-1]

if __name__  == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    solution = Solution()
    res = solution.construct_string(root)

    print(res)
