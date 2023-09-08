import collections


class TreeNode:
    def __init__(self, val =0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_depth(self, root):
        if not root:
            return 0

        q = collections.deque([root])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level +=1
        return level


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()

    res = solution.max_depth(root)

    print(res)