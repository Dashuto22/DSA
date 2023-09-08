class TreeNode:
    def __init__(self, val=0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameter(self, root):

        res = [0]

        def compute_diameter(root):
            if not root:
                return -1

            left = compute_diameter(root.left)
            right = compute_diameter(root.right)

            res[0] = max(res[0], left+right +2)

            return  1 + max(left,right)

        compute_diameter(root)

        return res[0]

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    res = solution.diameter(root)

    print(res)
