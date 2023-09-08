import collections

class TreeNode:
    def __init__(self, val =-1, left=None, right =None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def level_order_traversal(self, root):

        q = collections.deque([root] if root else [])

        res = []
        level = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                level += 1

        return res


if __name__ == '__main__':
    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)

    solution = Solution()

    res = solution.level_order_traversal(root)

    print(res)



