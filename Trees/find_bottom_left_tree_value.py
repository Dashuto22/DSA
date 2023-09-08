import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find_bottom_left_tree_val(self, root):
        q = collections.deque([root] if root else [])
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)

            if node.left:
                q.append(node.left)

        return node.val

if __name__ == '__main__':


