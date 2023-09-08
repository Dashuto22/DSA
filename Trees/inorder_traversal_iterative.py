class TreeNode:
    def __init__(self, val =0, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root):
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right =  TreeNode(5)


    solution = Solution()

    res = solution.inorder(root)

    print(res)