class TreeNode:
    def __init__(self, val =0, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def same_tree(self,p,q):
        if not p and not q:
            return True
        if (not p or not q) or (p.val !=q.val):
            return False

        return (self.same_tree(p.left, q.left) or self.same_tree(p.right, q.right))


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)

    solution = Solution()

    res = solution.same_tree(root, root2)

    print(res)