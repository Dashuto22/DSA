class TreeNode:
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def search(self, root, target):
        if not root:
            return False
        if root.val > target:
            return self.search(root.left, target)
        elif root.val < target:
            return self.search(root.right, target)
        else:
            return True

    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insert(root.left, val)
        elif root.val < val:
            root.right = self.insert(root.right, val)
        return root

    def minValNode(self, root):
        cur = root
        while cur and cur.left:
            cur = cur.left

        return cur.val

    def maxValNode(self, root):
        cur = root
        while cur and cur.right:
            cur = cur.right

        return cur.val

    def remove(self, root, val):
        if not root:
            return None
        if root.val > val:
            root.left = self.remove(root.left, val)

        elif root.val < val:
            root.right = self.remove(root.right, val)

        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minValNode(root.right)
                root.val = minNode.val
                root.right = self.remove(root.right,minNode.val)
        return root

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

        return root

    def preorder(self, root):
        if not root:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

        return root

    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)

        return root

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)

    root.left.left = TreeNode(1)
    root.right.right = TreeNode(5)

    sol = Solution()

    val = sol.search(root, 4)
    print(val)

    ins = sol.insert(root, 7)

    res = sol.inorder(root)

    rem = sol.remove(root, 1)

    print("after delete")

    res = sol.inorder(root)

    minm = sol.minValNode(root)

    print("min val", minm)

    maxm = sol.maxValNode(root)

    print("max val", maxm)


    pre = sol.preorder(root)


