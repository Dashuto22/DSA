class TreeNode:
    def __init__(self, val =0, left=None , right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert_into_bst(self, root, val):

        if not root:
            return TreeNode(val)

        if root.val >val:
            root.left = self.insert_into_bst(root.left, val)

        else:
            root.right = self.insert_into_bst(root.right, val)

        return root

