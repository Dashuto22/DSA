class TreeNode:
    def __init__(self, val=0, left= None, right= None):

        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanced_tree(self, root):
        def balanced(root):

            if not root:
                return [True, 0]

            left = balanced(root.left)
            right = balanced(root.right)

            balance = (left[0] and right[0] and abs(left[1]-right[1])<=1)

            return [balance, 1 + max(left[1], right[1])]

        return balanced(root)[0]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()

    res = solution.balanced_tree(root)

    print(res)