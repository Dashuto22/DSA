import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

class Solution:
    def check_completeness(self, root):

        q = collections.deque([root] if root else [])

        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)

            else:
                while q:
                    if q.popleft():
                        return False

        return True

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)

    sol = Solution()
    res = sol.check_completeness(root)

    print(res)