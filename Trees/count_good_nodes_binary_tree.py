class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

class Solution:
    def count_good_nodes(self,root):
        def dfs(node, maxval):
            if not node:
                return 0
            res = 1 if node.val >=maxval else 0
            maxval = max(maxval, node.val)
            res += dfs(node.left, maxval)
            res += dfs(node.right, maxval)

            return res

        return dfs(root, root.val)

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(1)
    root.left.left = TreeNode(3)

    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    solution = Solution()

    res = solution.count_good_nodes(root)

    print(res)