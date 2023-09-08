class TreeNode:
    def __init__(self, val =0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delete_node(self, root, key):
        if not root:
            return root
        if root.val > key:
            root.left = self.delete_node(root.left, key)
        elif root.val < key:
            root.right = self.delete_node(root.right, key)

        else:
            if not root.left:
                return root.right

            elif not root.right:
                return root.left
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left

                root.val = cur.val

                root.right = self.delete_node(root.rigt, cur.val)

            return root

if __name__ == '__main__':

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    solution = Solution()

    res = solution.delete_node(root, 3)

