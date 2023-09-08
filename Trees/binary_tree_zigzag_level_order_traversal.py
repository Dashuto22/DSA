import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val= val
        self.left = left
        self.right = right

class Solution:
    def binary_tree_zig_zag(self, root):
        res = []

        q = collections.deque([root] if root else [])

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level = reversed(level) if len(res)%2 else level
            res.append(level)

        return res

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)

    solution = Solution()

    res = solution.binary_tree_zig_zag(root)

    print(res)