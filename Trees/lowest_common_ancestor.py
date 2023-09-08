class TreeNode:
    def __init__(self, val=0, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lca(self, root, p,q):
        cur = root
        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left

            elif cur.val <p.val and cur.val < q.val:
                cur = cur.right

            else:
                return cur

if __name__ == '__main__':
    root = TreeNode(6)

    root.left = TreeNode(2)
    root.right = TreeNode(8)

    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)


    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)


    solution = Solution()

    p = TreeNode(2)
    q = TreeNode(8)

    res = solution.lca(root, p,q)

    print(res.val)