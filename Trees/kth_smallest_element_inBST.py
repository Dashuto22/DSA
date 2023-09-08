class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kth_smallest_elementBST(self, root,k):

        self.k = k
        self.result = None

        def dfs(node):
            if not node or self.result:
                return
            dfs(node.left)

            self.k -=1
            if self.k == 0:
                self.result = node.val

            dfs(node.right)

        dfs(root)

        return self.result


if __name__ == '__main__':
    root = TreeNode(3)
    root.right = TreeNode(4)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)

    sol = Solution()

    val = sol.kth_smallest_elementBST(root,1)

    print(val)